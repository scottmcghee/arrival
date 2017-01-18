import xmltodict
from synolopy import NasApi
import click
import json


@click.command()
@click.argument('webloc')
def signalsyno(webloc):
    try:
        #open the config file and read the config into a dict
        with open('conf.json') as conf_file:
            conf = json.load(conf_file)
        
        #open a connection to the NAS
        nas = NasApi(conf['nas_url'], conf['nas_username'], conf['nas_password'])

        #open the .webloc file passed from the workflow and read into a dict
        with open(webloc) as fd:
            webloc_contents = xmltodict.parse(fd.read())
        
        #grab the URL, determining where to insert username and password if necessary
        download_url = webloc_contents['plist']['dict']['string']
        if 'url_username' in conf and 'url_password' in conf:
            slice_point = 0
            if download_url.startswith('https'):
                slice_point = 8
            elif download_url.startswith('http'):
                slice_point = 7
            elif download_url.starswith('ftp'):
                slice_point = 6
            
            download_url = download_url[0:slice_point] + "{}:{}@".format(conf['url_username'], conf['url_password']) + download_url[slice_point:]

        #create a download task in Download Station
        nas.downloadstation.task.request('create', uri=download_url, destination=conf['nas_save_location'])
    except Exception as e:
        print e.message


if __name__ == "__main__":
    signalsyno()