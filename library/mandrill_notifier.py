from ansible.module_utils.basic import *


def main():
    argument_spec = {}
    argument_spec.update(
        dict(
            from_email={'required': True, 'type': 'str'},
            from_name={'required': True, 'type': 'str'},
            reply_to={'required': True, 'type': 'str'},
            html={'required': True, 'type': 'str'},
            subject={'required': True, 'type': 'str'},
            text={'required': True, 'type': 'str'},
            to={'required': True, 'type': 'str'},
            mandrill_notifier_api_token={'required': True, 'type': 'str'}
        ))

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)

    if not HAS_MANDRILL:
        module.fail_json(
            msg='mandrill is required. Install by '
                'running `pip install mandrill`')

    try:
        mandrill_client = mandrill.Mandrill(
            module.params['mandrill_notifier_api_token'])
        message = {
            'from_email': module.params['from_email'],
            'from_name': module.params['from_name'],
            'headers': {'Reply-To': module.params['reply_to']},
            'html': module.params['html'],
            'subject': module.params['subject'],
            'text': module.params['text'],
            'to': [{'email': module.params['to'], 'type': 'to'}]
        }

        result = mandrill_client.messages.send(message=message, async=False,
                                               ip_pool='Main Pool')
        module.exit_json(**{'changed': True, 'result': result})

    except mandrill.Error, e:
        module.fail_json(
            'A mandrill error occurred: %s - %s' % (e.__class__, e))

# if mandrill is installed
HAS_MANDRILL = False
try:
    import mandrill

    HAS_MANDRILL = True
except ImportError:
    HAS_MANDRILL = False

main()
