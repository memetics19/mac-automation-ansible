# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command to update fleet information."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.container.fleet import client
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.util.apis import arg_utils


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Update(base.UpdateCommand):
  """Update a fleet.

  This command can fail for the following reasons:
  * The project specified does not exist.
  * The project specified already has a fleet.
  * The active account does not have permission to access the given project.

  ## EXAMPLES

  To update the display name of the fleet in project `example-foo-bar-1`
  to `updated-name`, run:

    $ {command} --display-name=updated-name --project=example-foo-bar-1
  """

  @staticmethod
  def Args(parser):
    parser.add_argument(
        '--display-name',
        type=str,
        help='Display name of the fleet to be created (required). 4-30 '
        'characters, alphanumeric and [ \'"!-] only.',
        required=True)

  def Run(self, args):
    project = arg_utils.GetFromNamespace(args, '--project', use_defaults=True)
    fleetclient = client.FleetClient(release_track=base.ReleaseTrack.ALPHA)
    return fleetclient.UpdateFleet(args.display_name, project)
