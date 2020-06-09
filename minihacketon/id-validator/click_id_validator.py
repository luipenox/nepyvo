import click
from id_validator import valid_pid


@click.command()
@click.option('-p', '--pid', help='Czech Personal ID')
@click.option('-i', '--info', is_flag=True, help='Show more info (date and sex / error)')
def click_valid_pid(pid, info):
    values = valid_pid(pid, info)

    valid_text = f'--- ID {pid} is VALID ---'
    invalid_text = f'--- ID {pid} is INVALID ---'

    if info:
        if values[0]:
            click.echo(valid_text)
            click.echo(f"Year:  {values[1]['year']:4}")
            click.echo(f"Month: {values[1]['month']:4}")
            click.echo(f"Day:   {values[1]['day']:4}")
            click.echo(f"Sex:   {values[1]['sex']:>4}")
        else:
            click.echo(invalid_text)
            click.echo(f"Error: {values[1]}")
    else:
        if values:
            click.echo(valid_text)
        else:
            click.echo(invalid_text)


if __name__ == '__main__':
    click_valid_pid()
