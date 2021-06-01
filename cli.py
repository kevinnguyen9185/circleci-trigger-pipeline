import click
import http.client
import os


@click.command()
@click.option(
    '--branch',
    default='develop',
    help='Your branch to explicitly deploy'
)
@click.option(
    '--params',
    default='\"explicit_deploy\":true',
    help='Your company name'
)
@click.option(
    '--project',
    help="Project path from CircleCI company/project"
)
@click.option(
    '--tokenkey',
    default=os.getenv('CIRCLECI_TOKEN'),
    help='Personal API Key from CircleCI'
)
def trigger(branch, project, tokenkey, params):
    assert project is not None, "Project must be set explicitly"
    assert tokenkey is not None, "TokenKey must be set explicitly or via environment variable"
    conn = http.client.HTTPSConnection("circleci.com")
    
    payload = '{\"branch\":\"'+branch + \
        '\", \"parameters\":{'+params+'} }'
    print(payload)

    headers = {
        'content-type': "application/json",
        'Circle-Token': tokenkey
    }

    conn.request(
        "POST", f"/api/v2/project/gh/{project}/pipeline", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == '__main__':
    trigger()
