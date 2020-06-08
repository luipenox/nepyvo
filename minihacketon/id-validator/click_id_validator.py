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
            print(valid_text)
            print(f"Year:  {values[1]['year']:4}")
            print(f"Month: {values[1]['month']:4}")
            print(f"Day:   {values[1]['day']:4}")
            print(f"Sex:   {values[1]['sex']:>4}")
        else:
            print(invalid_text)
            print(f"Error: {values[1]}")
    else:
        if values[0]:
            print(valid_text)
        else:
            print(invalid_text)


if __name__ == '__main__':
    click_valid_pid()
