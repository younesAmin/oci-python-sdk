# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

##########################################################################
# multi_tag_resources_in_tenancy.py
#
# @author: Adi Zohar
#
# Supports Python  3
#
# DISCLAIMER - This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes
##########################################################################
# Info:
#    Tag Resources in Tenancy
#
# Connectivity:
#    Option 1 - User Authentication
#       $HOME/.oci/config, please follow - https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm
#    Option 2 - Instance Principle
#    Option 3 - Token Delegation using cloud shell
#
##########################################################################
# Modules Included:
# - oci.core.ComputeClient
# - oci.core.BlockstorageClient
# - oci.core.VirtualNetworkClient
# - oci.identity.IdentityClient
# - oci.load_balancer.LoadBalancerClient
# - oci.database.DatabaseClient
# - oci.object_storage.ObjectStorageClient
#
##########################################################################
# Application Command line parameters
#
#   -t config       - Config file section to use (tenancy profile)
#   -p proxy        - Set Proxy (i.e. www-proxy-server.com:80)
#   -ip             - Use Instance Principals for Authentication
#   -dt             - Use Instance Principals with delegation token for cloud shell
#   -cp compartment - filter by compartment name or id
#   -rg region      - filter by region name
#   -action add_defined | add_free | del_defined | del_free | list
#   -tag            - tag information, can be either namespace.key=value or key=value with comma seperator for multiple tags
#   -tagsep         - tag seperator default comma
#   -force          - don't confirm execution
#   -service type   - Service Type default all, Services = all,compute,block,network,identity,loadbalancer,database,object,file
#   -output         - list | json | summary
#   -filter_by_name - Filter service by name, comma seperator for multi names
##########################################################################

import sys
import argparse
import datetime
import oci
import json
import os

# global variables
errors = 0
data = []
cmd = ""


##########################################################################
# Print banner
##########################################################################
def print_banner(cmd, tenancy, assign_tags):
    print_header("Running Tag Resources")
    print("Written By Adi Zohar, Feb 2022")
    print("Starts at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("Command Line  : " + ' '.join(x for x in sys.argv[1:]))
    if cmd.tag:
        for index, arr in enumerate(assign_tags, start=1):
            tag_str = (arr['namespace'] + "." if arr['namespace'] else "") + arr['key'] + "=" + arr['value']
            print("Tag " + str(index) + "         : " + tag_str)
    print("Tag Seperator : " + str(cmd.tagseperator))
    print("Tenant Name   : " + str(tenancy.name))
    print("Tenant Id     : " + tenancy.id)
    print("Services      : " + cmd.service)
    if cmd.filter_by_name:
        print("Filter by Name: " + cmd.filter_by_name)


##########################################################################
# Print header centered
##########################################################################
def print_header(name):
    chars = int(90)
    print("")
    print('#' * chars)
    print("#" + name.center(chars - 2, " ") + "#")
    print('#' * chars)


##########################################################################
# convert dict to string for printing
##########################################################################
def get_string_dict(dic, namespace=False):
    retval = ""

    # if not dictionary
    if dic is None or dic == "":
        return retval

    # if namespace
    if namespace:
        for key, val in dic.items():
            if len(retval) > 0:
                retval += ", "
            retval += ", ".join("{}.{}={}".format(key, k, v) for k, v in val.items())
    # if free
    else:
        retval = ', '.join("{}={}".format(k, v) for k, v in dic.items())
    return retval


##########################################################################
# Handle Tag
##########################################################################
def command_line():
    global cmd
    cmd_assign_tags = []

    try:
        # Get Command Line Parser
        parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=80, width=170))
        parser.add_argument('-t', default="", dest='config_profile', help='Config file section to use (tenancy profile)')
        parser.add_argument('-p', default="", dest='proxy', help='Set Proxy (i.e. www-proxy-server.com:80) ')
        parser.add_argument('-cp', default="", dest='compartment', help='Filter by Compartment Name or Id')
        parser.add_argument('-rg', default="", dest='region', help='Filter by Region Name')
        parser.add_argument('-ip', action='store_true', default=False, dest='is_instance_principals', help='Use Instance Principals for Authentication')
        parser.add_argument('-dt', action='store_true', default=False, dest='is_delegation_token', help='Use Delegation Token for Authentication')
        parser.add_argument('-tag', default="", dest='tag', help='Tags in format - namespace.key=value or key=value with comma seperator for multi tags')
        parser.add_argument('-tagseperator', default=",", dest='tagseperator', help='Tag Seperator for multiple tags, default=,')
        parser.add_argument('-action', default="", dest='action', choices=['add_defined', 'add_free', 'del_defined', 'del_free', 'list'], help='Action Type')
        parser.add_argument('-output', default="list", dest='output', choices=['list', 'json', 'summary'], help='Output type, default=summary')
        parser.add_argument('-service', default="all", dest='service', help='Services = all,compute,block,network,identity,loadbalancer,database,object,file. default=all')
        parser.add_argument('-force', default=False, action='store_true', dest='force', help='Force execution (do not confirm)')
        parser.add_argument('-filter_by_name', default="", dest='filter_by_name', help='Filter service by name comma seperator for multi')
        cmd = parser.parse_args()

        # Check if action
        if not (cmd.action):
            parser.print_help()
            print("\nYou must specify action !!")
            raise SystemExit

        # Check if any tag specified with action add or del
        if (cmd.action == "add_defined" or cmd.action == "add_free" or cmd.action == "del_defined" or cmd.action == "del_free") and not cmd.tag:
            parser.print_help()
            print("\nYou must specify tag to add or delete !!")
            raise SystemExit

        # if defined tag
        if ("defined" in cmd.action):
            for tag in cmd.tag.split(cmd.tagseperator):
                assign_tag_namespace = tag.split(".")[0]
                assign_tag_key = tag.split(".")[1].split("=")[0]
                assign_tag_value = tag.split("=")[1]
                if not (assign_tag_namespace or assign_tag_key or assign_tag_value):
                    print("Error with tag format, must be in format - namespace.key=value")
                    raise SystemExit
                cmd_assign_tags.append({
                    'namespace': assign_tag_namespace,
                    'key': assign_tag_key,
                    'value': assign_tag_value
                })

        # if freeform tag
        if ("free" in cmd.action):
            for tag in cmd.tag.split(","):
                assign_tag_key = tag.split("=")[0]
                assign_tag_value = tag.split("=")[1]
                if not (assign_tag_key or assign_tag_value):
                    print("Error with tag format, must be in format - key=value")
                    raise SystemExit
                cmd_assign_tags.append({
                    'namespace': "",
                    'key': assign_tag_key,
                    'value': assign_tag_value
                })

        # return the command line
        return cmd, cmd_assign_tags

    except Exception as e:
        raise RuntimeError("Error in command_line: " + str(e.args))


##########################################################################
# check service error to warn instead of error
##########################################################################
def check_service_error(code):
    return ('max retries exceeded' in str(code).lower() or
            'auth' in str(code).lower() or
            'notfound' in str(code).lower() or
            code == 'Forbidden' or
            code == 'TooManyRequests' or
            code == 'IncorrectState' or
            code == 'LimitExceeded'
            )


##########################################################################
# Create signer for Authentication
# Input - config_profile and is_instance_principals and is_delegation_token
# Output - config and signer objects
##########################################################################
def create_signer(config_profile, is_instance_principals, is_delegation_token):

    # if instance principals authentications
    if is_instance_principals:
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
            config = {'region': signer.region, 'tenancy': signer.tenancy_id}
            return config, signer

        except Exception:
            print_header("Error obtaining instance principals certificate, aborting")
            raise SystemExit

    # -----------------------------
    # Delegation Token
    # -----------------------------
    elif is_delegation_token:

        try:
            # check if env variables OCI_CONFIG_FILE, OCI_CONFIG_PROFILE exist and use them
            env_config_file = os.environ.get('OCI_CONFIG_FILE')
            env_config_section = os.environ.get('OCI_CONFIG_PROFILE')

            # check if file exist
            if env_config_file is None or env_config_section is None:
                print("*** OCI_CONFIG_FILE and OCI_CONFIG_PROFILE env variables not found, abort. ***")
                print("")
                raise SystemExit

            # check if file exist
            if not os.path.isfile(env_config_file):
                print("*** Config File " + env_config_file + " does not exist, Abort. ***")
                print("")
                raise SystemExit

            config = oci.config.from_file(env_config_file, env_config_section)
            delegation_token_location = config["delegation_token_file"]

            with open(delegation_token_location, 'r') as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
                # get signer from delegation token
                signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)

                return config, signer

        except KeyError:
            print("* Key Error obtaining delegation_token_file")
            raise SystemExit

        except Exception:
            raise

    # -----------------------------
    # config file authentication
    # -----------------------------
    else:
        config = oci.config.from_file(
            oci.config.DEFAULT_LOCATION,
            (config_profile if config_profile else oci.config.DEFAULT_PROFILE)
        )
        signer = oci.signer.Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=oci.config.get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        return config, signer


##########################################################################
# Check if tag namespace exist
##########################################################################
def read_tag_namespaces(identity, tenancy, local_assign_tags):
    try:
        print("\nReading Tag Namespaces...")
        tag_namespaces = oci.pagination.list_call_get_all_results(
            identity.list_tag_namespaces,
            tenancy.id,
            include_subcompartments=True,
            lifecycle_state='ACTIVE'
        ).data

        ##########################################
        # check if namespace exit for each tag
        ##########################################
        for tag_array in local_assign_tags:
            assign_tag_namespace_obj = None
            for tag_namespace in tag_namespaces:
                if tag_namespace.name == tag_array['namespace']:
                    assign_tag_namespace_obj = tag_namespace
                    print("   Found Tag Namespace '" + tag_array['namespace'] + "', id = " + tag_namespace.id)
                    break

            if not assign_tag_namespace_obj:
                print("Could not find tag namespace " + tag_array['namespace'])
                print("Abort.")
                raise SystemExit

            # check tag key
            tags = oci.pagination.list_call_get_all_results(
                identity.list_tags,
                assign_tag_namespace_obj.id,
                lifecycle_state='ACTIVE'
            ).data

            tag_key_found = False
            for tag in tags:
                if tag.name == tag_array['key']:
                    tag_key_found = True
                    print("   Found Tag Key '" + tag_array['key'] + "', id = " + tag.id)
                    break

            if not tag_key_found:
                print("Could not find tag Key " + tag_array['key'])
                print("Abort.")
                raise SystemExit

    except Exception as e:
        raise RuntimeError("\nError checking tag namespaces - " + str(e))


##########################################################################
# Load compartments
##########################################################################
def identity_read_compartments(identity, tenancy):

    global cmd
    print("Loading Compartments...")
    try:
        compartments = oci.pagination.list_call_get_all_results(
            identity.list_compartments,
            tenancy.id,
            compartment_id_in_subtree=True,
        ).data

        # Add root compartment which is not part of the list_compartments
        compartments.append(tenancy)

        # compile new compartment object
        filtered_compartment = []
        for compartment in compartments:
            # skip non active compartments
            if compartment.id != tenancy.id and compartment.lifecycle_state != oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                continue

            # if filter by compartment name or id if specified
            if cmd.compartment:
                if compartment.id != cmd.compartment and compartment.name != cmd.compartment:
                    continue

            filtered_compartment.append(compartment)

        print("    Total " + str(len(filtered_compartment)) + " compartments loaded.")
        return filtered_compartment

    except Exception as e:
        raise RuntimeError("Error in identity_read_compartments: " + str(e.args))


##########################################################################
# Handle Object
##########################################################################
def handle_object(compartment, region_name, assign_tags, obj_name, list_object, update_object, update_modal_obj, availability_domains=None, namespace="", filter_by_name=""):

    global data
    global errors

    try:
        cnt = 0
        cnt_added = 0
        cnt_deleted = 0
        cnt_exist = 0
        cnt_updated = 0

        # if AD generate ad names
        availability_domains_array = [ad.name for ad in availability_domains] if availability_domains else ['single']

        # call the API
        array = []
        for availability_domain in availability_domains_array:
            try:
                if availability_domains:
                    array = oci.pagination.list_call_get_all_results(list_object, availability_domain=availability_domain, compartment_id=compartment.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                elif namespace:
                    array = oci.pagination.list_call_get_all_results(list_object, namespace, compartment.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY, fields=['tags']).data
                else:
                    array = oci.pagination.list_call_get_all_results(list_object, compartment_id=compartment.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
            except oci.exceptions.ServiceError as e:
                if check_service_error(e.code):
                    errors += 1
                    print("        " + obj_name + " ...errors ")
                    return
                raise

            # loop on Array
            for arr in array:
                if not namespace and obj_name != "Network CPEs":
                    if arr.lifecycle_state == "TERMINATING" or arr.lifecycle_state == "TERMINATED":
                        continue

                # object id - diff between services
                object_name = str(arr.name) if namespace else str(arr.display_name)
                obj_id = str(arr.name) if namespace else str(arr.id)

                # if filter by name - comma seperated
                if filter_by_name:
                    found = False
                    for name in filter_by_name.split(","):
                        if object_name == name:
                            found = True
                    if not found:
                        continue

                defined_tags, freeform_tags, tags_added, tags_deleted, tags_exist, tags_updated = handle_tags(arr.defined_tags, arr.freeform_tags, assign_tags)

                # if tag modified:
                if tags_added > 0 or tags_deleted > 0 or tags_updated > 0:

                    # if object storage
                    if namespace:
                        update_object(namespace, obj_id, update_modal_obj(freeform_tags=freeform_tags, defined_tags=defined_tags), retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
                    elif obj_name == "Load Balancers":
                        update_object(update_modal_obj(freeform_tags=freeform_tags, defined_tags=defined_tags), obj_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)
                    else:
                        update_object(obj_id, update_modal_obj(freeform_tags=freeform_tags, defined_tags=defined_tags), retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY)

                ############################################
                # Add data to array
                ############################################
                value = ({
                    'region_name': region_name,
                    'compartment_name': str(compartment.name),
                    'type': obj_name,
                    'id': obj_id,
                    'display_name': str(arr.name) if namespace else str(arr.display_name),
                    'defined_tags': defined_tags,
                    'freeform_tags': freeform_tags,
                    'tags_added': tags_added,
                    'tags_deleted': tags_deleted,
                    'tags_updated': tags_updated,
                    'tags_exist': tags_exist
                })

                data.append(value)
                cnt += 1
                cnt_added += tags_added
                cnt_deleted += tags_deleted
                cnt_exist += tags_exist
                cnt_updated += tags_updated

        # print count
        if cnt == 0:
            print("        " + obj_name.ljust(22) + " - (-)")
        elif "del" in cmd.action:
            print("        " + obj_name.ljust(22) + " - " + str(cnt).ljust(5) + str(" Tag Deleted = " + str(cnt_deleted)).ljust(22) + " Tag Exist = " + str(cnt_exist))
        elif "add" in cmd.action:
            print("        " + obj_name.ljust(22) + " - " + str(cnt).ljust(5) + str(" Tag Added = " + str(cnt_added)).ljust(22) + str(" Tag Updated = " + str(cnt_updated)).ljust(22) + " Tag Exist = " + str(cnt_exist))
        else:
            print("        " + obj_name.ljust(22) + " - " + str(cnt))

    except Exception as e:
        print("Error in handle_object: " + obj_name + " " + str(e.args))
        errors += 1


##########################################################################
# Handle Tag
##########################################################################
def handle_tags(defined_tags, freeform_tags, local_assign_tags):
    try:
        local_tags_added = 0
        local_tags_deleted = 0
        local_tags_exist = 0
        local_tags_updated = 0

        ############################################
        # handle defined tags
        ############################################
        if "defined" in cmd.action:
            for array_tag in local_assign_tags:
                assign_tag_namespace = array_tag['namespace']
                assign_tag_key = array_tag['key']
                assign_tag_value = array_tag['value']
                defined_tags_exist = False

                if defined_tags:
                    if assign_tag_namespace in defined_tags:
                        if assign_tag_key in defined_tags[assign_tag_namespace]:
                            if defined_tags[assign_tag_namespace][assign_tag_key] == assign_tag_value:
                                defined_tags_exist = True
                                local_tags_exist += 1

                # Del Key
                if "del" in cmd.action:
                    if defined_tags_exist:
                        # remove the key value
                        defined_tags[assign_tag_namespace].pop(assign_tag_key, None)
                        # dict is empty
                        if not defined_tags[assign_tag_namespace]:
                            defined_tags.pop(assign_tag_namespace, None)
                        local_tags_deleted += 1

                # Add or update Key
                else:
                    if not defined_tags_exist:
                        if not defined_tags:
                            defined_tags = {}

                        # if namespace exist, add or update to the dict.
                        if assign_tag_namespace in defined_tags:
                            if assign_tag_key in defined_tags[assign_tag_namespace]:
                                if defined_tags[assign_tag_namespace][assign_tag_key] != assign_tag_value:
                                    defined_tags[assign_tag_namespace][assign_tag_key] = assign_tag_value
                                    local_tags_updated += 1
                            else:
                                defined_tags[assign_tag_namespace][assign_tag_key] = assign_tag_value
                                local_tags_added += 1
                        else:
                            defined_tags[assign_tag_namespace] = {assign_tag_key: assign_tag_value}
                            local_tags_added += 1

        ############################################
        # handle freeform tags
        ############################################
        if "free" in cmd.action:
            for array_tag in local_assign_tags:
                assign_tag_key = array_tag['key']
                assign_tag_value = array_tag['value']
                freeform_tags_exist = False

                if freeform_tags:
                    if assign_tag_key in freeform_tags:
                        if freeform_tags[assign_tag_key] == assign_tag_value:
                            freeform_tags_exist = True
                            local_tags_exist += 1

                # Del Key
                if "del" in cmd.action:
                    if freeform_tags_exist:
                        freeform_tags.pop(assign_tag_key, None)
                        local_tags_deleted += 1

                # Add Key
                else:
                    if not freeform_tags_exist:
                        if not freeform_tags:
                            freeform_tags = {}
                        if assign_tag_key in freeform_tags:
                            if freeform_tags[assign_tag_key] != assign_tag_value:
                                freeform_tags[assign_tag_key] = assign_tag_value
                                local_tags_updated += 1
                        else:
                            freeform_tags[assign_tag_key] = assign_tag_value
                            local_tags_added += 1

        # return modified tags
        return defined_tags, freeform_tags, local_tags_added, local_tags_deleted, local_tags_exist, local_tags_updated

    except Exception as e:
        raise RuntimeError("Error in handle_tags: " + str(e.args))


##########################################################################
# Main
##########################################################################
def main():
    global data
    cmd, assign_tags = command_line()

    # Identity extract compartments
    config, signer = create_signer(cmd.config_profile, cmd.is_instance_principals, cmd.is_delegation_token)
    compartments = []
    tenancy = None
    try:
        print("\nConnecting to Identity Service...")
        identity = oci.identity.IdentityClient(config, signer=signer)
        if cmd.proxy:
            identity.base_client.session.proxies = {'https': cmd.proxy}

        tenancy = identity.get_tenancy(config["tenancy"]).data
        regions = identity.list_region_subscriptions(tenancy.id).data
        compartments = identity_read_compartments(identity, tenancy)

    except Exception as e:
        raise RuntimeError("\nError extracting compartments section - " + str(e))

    ############################################
    # Print Banner
    ############################################
    print_banner(cmd, tenancy, assign_tags)

    ############################################
    # Check if Tag namespace exist
    ############################################
    if "defined" in cmd.action and cmd.tag:
        read_tag_namespaces(identity, tenancy, assign_tags)

    ############################################
    # Confirm
    ############################################
    confirm = "yes" if cmd.force else ""
    if not cmd.force:
        confirm = input("\nType yes to execute: ")

    if confirm.lower() != "yes":
        sys.exit()

    ############################################
    # Loop on all regions
    ############################################
    print("\nProcessing Regions...")
    data = []
    errors = 0
    for region_name in [str(es.region_name) for es in regions]:

        # check if filter by region
        if cmd.region:
            if cmd.region not in region_name:
                continue

        print("\nRegion " + region_name + "...")

        # set the region in the config and signer
        config['region'] = region_name
        signer.region = region_name

        # connect to ComputeClient
        compute_client = oci.core.ComputeClient(config, signer=signer)
        blockstorage_client = oci.core.BlockstorageClient(config, signer=signer)
        network_client = oci.core.VirtualNetworkClient(config, signer=signer)
        identity_client = oci.identity.IdentityClient(config, signer=signer)
        loadbalancer_client = oci.load_balancer.LoadBalancerClient(config, signer=signer)
        database_client = oci.database.DatabaseClient(config, signer=signer)
        objectstorage_client = oci.object_storage.ObjectStorageClient(config, signer=signer)
        filestorage_client = oci.file_storage.FileStorageClient(config, signer=signer)

        # If proxy
        if cmd.proxy:
            compute_client.base_client.session.proxies = {'https': cmd.proxy}
            blockstorage_client.base_client.session.proxies = {'https': cmd.proxy}
            network_client.base_client.session.proxies = {'https': cmd.proxy}
            identity_client.base_client.session.proxies = {'https': cmd.proxy}
            loadbalancer_client.base_client.session.proxies = {'https': cmd.proxy}
            database_client.base_client.session.proxies = {'https': cmd.proxy}
            objectstorage_client.base_client.session.proxies = {'https': cmd.proxy}
            filestorage_client.base_client.session.proxies = {'https': cmd.proxy}

        # get availability_domains for the region
        availability_domains = identity_client.list_availability_domains(tenancy.id).data

        # get namespace for object storage
        namespace = objectstorage_client.get_namespace().data

        # filter by name variable
        filter_by_name = cmd.filter_by_name if cmd.filter_by_name else ""

        ############################################
        # Loop on all compartments for instances
        ############################################
        try:
            for compartment in compartments:

                print("    Compartment " + str(compartment.name))

                # Compute
                if "all" in cmd.service or "compute" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "Instances", compute_client.list_instances, compute_client.update_instance, oci.core.models.UpdateInstanceDetails, filter_by_name=filter_by_name)

                # Block storage
                if "all" in cmd.service or "block" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "Boot Volumes", blockstorage_client.list_boot_volumes, blockstorage_client.update_boot_volume, oci.core.models.UpdateBootVolumeDetails, availability_domains, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Boot Volumes Backups", blockstorage_client.list_boot_volume_backups, blockstorage_client.update_boot_volume_backup, oci.core.models.UpdateBootVolumeBackupDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Block Volumes", blockstorage_client.list_volumes, blockstorage_client.update_volume, oci.core.models.UpdateVolumeDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Block Volumes Backups", blockstorage_client.list_volume_backups, blockstorage_client.update_volume_backup, oci.core.models.UpdateVolumeBackupDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Volume Groups", blockstorage_client.list_volume_groups, blockstorage_client.update_volume_group, oci.core.models.UpdateVolumeGroupDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Volume Groups Backup", blockstorage_client.list_volume_group_backups, blockstorage_client.update_volume_group_backup, oci.core.models.UpdateVolumeGroupBackupDetails, filter_by_name=filter_by_name)

                # filestorage
                if "all" in cmd.service or "file" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "File Systems", filestorage_client.list_file_systems, filestorage_client.update_file_system, oci.file_storage.models.UpdateFileSystemDetails, availability_domains, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Mount Targets", filestorage_client.list_mount_targets, filestorage_client.update_mount_target, oci.file_storage.models.UpdateMountTargetDetails, availability_domains, filter_by_name=filter_by_name)

                # Network
                if "all" in cmd.service or "network" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "Network VCNs", network_client.list_vcns, network_client.update_vcn, oci.core.models.UpdateVcnDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network Subnets", network_client.list_subnets, network_client.update_subnet, oci.core.models.UpdateSubnetDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network CPEs", network_client.list_cpes, network_client.update_cpe, oci.core.models.UpdateCpeDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network DHCPs", network_client.list_dhcp_options, network_client.update_dhcp_options, oci.core.models.UpdateDhcpDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network IGWs", network_client.list_internet_gateways, network_client.update_internet_gateway, oci.core.models.UpdateInternetGatewayDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network IPSECs", network_client.list_ip_sec_connections, network_client.update_ip_sec_connection, oci.core.models.UpdateIPSecConnectionDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network LPGs", network_client.list_local_peering_gateways, network_client.update_local_peering_gateway, oci.core.models.UpdateLocalPeeringGatewayDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network NATGWs", network_client.list_nat_gateways, network_client.update_nat_gateway, oci.core.models.UpdateNatGatewayDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network RPGs", network_client.list_remote_peering_connections, network_client.update_remote_peering_connection, oci.core.models.UpdateRemotePeeringConnectionDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network Routes", network_client.list_route_tables, network_client.update_route_table, oci.core.models.UpdateRouteTableDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network SLs", network_client.list_security_lists, network_client.update_security_list, oci.core.models.UpdateSecurityListDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network SGWs", network_client.list_service_gateways, network_client.update_service_gateway, oci.core.models.UpdateServiceGatewayDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "Network VCircuit", network_client.list_virtual_circuits, network_client.update_virtual_circuit, oci.core.models.UpdateVirtualCircuitDetails, filter_by_name=filter_by_name)

                # load balancer
                if "all" in cmd.service or "loadbalancer" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "Load Balancers", loadbalancer_client.list_load_balancers, loadbalancer_client.update_load_balancer, oci.load_balancer.models.UpdateLoadBalancerDetails, filter_by_name=filter_by_name)

                # Databases
                if "all" in cmd.service or "database" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "DB DB Systems", database_client.list_db_systems, database_client.update_db_system, oci.database.models.UpdateDbSystemDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "DB Autonomous", database_client.list_autonomous_databases, database_client.update_autonomous_database, oci.database.models.UpdateAutonomousDatabaseDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "DB ExaCS Infra", database_client.list_cloud_exadata_infrastructures, database_client.update_cloud_exadata_infrastructure, oci.database.models.UpdateCloudExadataInfrastructureDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "DB ExaCS VM Cluster", database_client.list_cloud_vm_clusters, database_client.update_cloud_vm_cluster, oci.database.models.UpdateCloudVmClusterDetails, filter_by_name=filter_by_name)
                    handle_object(compartment, region_name, assign_tags, "DB Homes", database_client.list_db_homes, database_client.update_db_home, oci.database.models.UpdateDbHomeDetails, filter_by_name=filter_by_name)

                # Object storage
                if "all" in cmd.service or "object" in cmd.service:
                    handle_object(compartment, region_name, assign_tags, "Object Storage Buckets", objectstorage_client.list_buckets, objectstorage_client.update_bucket, oci.object_storage.models.UpdateBucketDetails, namespace=namespace, filter_by_name=filter_by_name)

        except Exception as e:
            raise RuntimeError("\nError extracting Instances - " + str(e))

    ############################################
    # Print Output as JSON
    ############################################
    if cmd.output == "json":
        print_header("Output as JSON")
        print(json.dumps(data, indent=4, sort_keys=False))

    if cmd.output == "list":
        print_header("Output as List")
        for item in data:
            print(
                item['region_name'].ljust(12) + " | " +
                item['compartment_name'].ljust(20) + " | " +
                item['type'].ljust(24) + " | " +
                str('Added: ' + str(item['tags_added'])).ljust(12) + " | " +
                str('Updated: ' + str(item['tags_updated'])).ljust(12) + " | " +
                str('Deleted: ' + str(item['tags_deleted'])).ljust(12) + " | " +
                str('Exist: ' + str(item['tags_exist'])).ljust(12) + " | " +
                item['display_name'].ljust(20) + " | " +
                get_string_dict(item['freeform_tags']) + " | " +
                get_string_dict(item['defined_tags'], True)
            )

    if errors > 0:
        print_header(str(errors) + " errors appeared")
    print_header("Completed at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


############################################
# Execute
############################################
main()
