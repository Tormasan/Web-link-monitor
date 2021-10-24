import yaml
import time
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def yaml_loader(filepath: str):
    """loading the yaml file"""
    with open(filepath, "r") as file_descriptor:
        yaml_data = yaml.safe_load(file_descriptor)
    return yaml_data


def reachable(Request: str):
    """Request if a site is reachable """
    try:
        response = urlopen(Request)
    except HTTPError as e:
        get_reachable_string = 'The server couldn\'t fulfill the request. Error code: ', e.code
    except URLError as e:
        get_reachable_string = 'UNREACHABLE. Reason:', e.reason
    else:
        get_reachable_string = ('REACHABLE')
    return get_reachable_string

if __name__ == "__main__":
    filepath ="conf.yml"
    data = yaml_loader(filepath)
    refresh_time = data.get('monitorInterval')

    while (True):
        for url in data.get('urls'):
            local_dt = datetime.now()
            urlre = reachable(url)
            print(local_dt.strftime("%A %d %b %Y %H:%M:%S %p CEST,"), url,",", urlre)
        time.sleep(refresh_time)

