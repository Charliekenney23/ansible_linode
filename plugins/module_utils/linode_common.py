from __future__ import absolute_import, division, print_function
__metaclass__ = type

import traceback

try:
    from ansible.module_utils.ansible_release import __version__ as ANSIBLE_VERSION
except Exception:
    ANSIBLE_VERSION = 'unknown'

from ansible.module_utils.basic import AnsibleModule, missing_required_lib, env_fallback

try:
  from linode_api4 import LinodeClient
  HAS_LINODE = True
except ImportError:
  HAS_LINODE = False
  HAS_LINODE_EXC = traceback.format_exc()


ANSIBLE_USER_AGENT = 'Ansible/{0}'.format(ANSIBLE_VERSION)


LINODE_COMMON_ARGS = dict(
  api_token=dict(
    type='str',
    fallback=(env_fallback, ['LINODE_API_TOKEN', 'LINODE_TOKEN']),
    required=True,
    no_log=True
  ),
  api_version=dict(
    type='str',
    fallback=(env_fallback, ['LINODE_API_VERSION']),
    default='v4'
  ),
  state=dict(
    type='str',
    required=True,
    choices=['present', 'absent'],
  ),
)


LINODE_TAG_ARGS = dict(
  tags=dict(type='list'),
)


LINODE_LABEL_ARGS = dict(
  label=dict(type='str', required=True),
)


class LinodeModuleBase(object):
  """A base for all Linode resource modules."""

  def __init__(self, module_arg_spec, supports_tags=True, has_label=True, bypass_checks=False,
    no_log=False, mutually_exclusive=None, required_together=None, required_one_of=None,
    add_file_common_args=False, supports_check_mode=False, required_if=None, skip_exec=False):

    arg_spec = dict()
    arg_spec.update(module_arg_spec)
    arg_spec.update(LINODE_COMMON_ARGS)

    if has_label:
      arg_spec.update(LINODE_LABEL_ARGS)

    if supports_tags:
      arg_spec.update(LINODE_TAG_ARGS)

    self._client = None
    self.module = AnsibleModule(argument_spec=arg_spec, bypass_checks=bypass_checks, no_log=no_log,
      mutually_exclusive=mutually_exclusive, required_together=required_together,
      required_one_of=required_one_of, add_file_common_args=add_file_common_args,
      supports_check_mode=supports_check_mode, required_if=required_if)

    if not HAS_LINODE:
      self.fail(msg=missing_required_lib('linode_api4'), exception=HAS_LINODE_EXC)

    if not skip_exec:
      res = self.exec_module(**self.module.params)
      self.module.exit_json(**res)

  def fail(self, msg, **kwargs):
    '''
    Shortcut for calling module.fail

    :param msg: Error message
    :param kwargs: Any key=value pairs
    :return: None
    '''
    self.module.fail_json(msg=msg, **kwargs)

  def exec_module(self, **kwargs):
    self.fail("Error: module {0} not implemented".format(self.__class__.__name__))

  @property
  def client(self):
    if not self._client:
      api_token = self.module.params['api_token']
      api_version = self.module.params['api_version']

      self._client = LinodeClient(
        api_token,
        base_url='https://api.linode.com/{0}'.format(api_version),
        user_agent=ANSIBLE_USER_AGENT,
      )

    return self._client
