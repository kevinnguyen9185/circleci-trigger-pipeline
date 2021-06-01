# cideploy

Cideploy is a Python based cli to trigger a CircleCI pipeline

# TL;DR

CircleCI is lighweight and handy tool for CI/CD. However, as it is quite new and less functionalities.
One of the big pain point during development is lack of deployment without updating the `config.yml`

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
virtualenv venv
. venv/bin/activate
pip install --editable .
```

## CLI Usage

```bash
export CIRCLECI_TOKEN=xxxx #xxxx is the personal API key retrived from CircleCI
cideploy --branch=xxx --project=company/project --params=\"explicit_deploy\":true
```

## CircleCI config.yml

Make sure you introduce a pipeline param to filter deployment by job.

In this example I introduce `explicit_deploy` which will differentiate between `main` and `deploy` workflow.

`main` is default workflow while `deploy` is a workflow only trigger when `explicit_deploy` is set to True. This place where `cideploy` becomes handy.

```yaml
version: 2.1

parameters:
  explicit_deploy:
    type: boolean
    default: false

jobs:
  deploy_git_source:
    machine:
      image: ubuntu-1604:201903-01
    steps:
      - echo_pipeline_info
      - run:
          name: Deploy with git source
          command: |

workflows:
  main:
    when:
      condition:
        - not: <<pipeline.parameters.explicit_deploy>>
    jobs:
      - deploy_git_source:
          filters:
            branches:
              only: develop
          requires:
            - test_integration

  deploy:
    when: <<pipeline.parameters.explicit_deploy>>
    jobs:
      - test_unit
      - deploy_git_source:
          requires:
            - test_unit
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)