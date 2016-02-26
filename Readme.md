ansible-mandrill
===============

An ansible role and library that uses [mandrill](https://www.mandrill.com/) to send emails.

### Role Variables
```yaml
mandrill_notifier_to            : "coolguy@example.com"
mandrill_notifier_from_email    : "email@example.com"
mandrill_notifier_from_name     : "Sender Name"
mandrill_notifier_reply_to      : "noreply@example.com"
mandrill_notifier_subject       : "Subject Something"
mandrill_notifier_html          : "noreply@example.com"
mandrill_notifier_text          : "Some text"
mandrill_notifier_api_token     : "Your API token"

# If you want to send a list of users. uses with_items
mandrill_notifier_list_users    : [ "list" ]
```

## License
MIT

### Contributors
* [Mohannad Ali](https://github.com/mandoz)
