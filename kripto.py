from bitcoinrpc.authproxy import AuthServiceProxy
from bitcoin import *  
from blockchain import exchangerates
import PySimpleGUI as sg


CLIENT_URL = 'http://student:2B4DB3SmsM2B4DB3SmsM89QjgYFp89QjgYFp@blockchain.oss.unist.hr:8332'


def layout():
    
    sg.theme('DarkBlue14')
    layout = [[sg.Button('Generate private key', key='private_key'), sg.Button('Generate public key', key='public_key'), sg.Button('Create a bitcoin address', key='address')],
              [sg.Button('Get statistics about transactions in the chain', key='statistic')],
              [sg.Text('Get statistics about block, enter the height of the block:'), sg.InputText(key='high'),sg.Button('Get statistic')],          
              [sg.Text('Get the Bitcoin rates in various currencies:'), sg.Button('Exchange rates', key='rates')], 
              [sg.Text('Enter the address:'), sg.InputText(key='adresa'),sg.Button('View address transaction history', key='history')],
              [sg.Image('C:/Users/korisnik/Desktop/blockchain.png', size=(800,300))],
              [sg.Cancel()]
              ]
    return layout

def transactions_statistic():

    client = AuthServiceProxy(CLIENT_URL)
    info = client.getchaintxstats()
    data = ''
    for key, item in info.items():
        data += str(key) + ' : ' + str(item).replace('{', '').replace('}', '').replace("'", '').replace(',', ', ').title()+'\n'
    sg.popup(data, title='Statistics about transactions in the chain')

def block_statistic(high):

    client = AuthServiceProxy(CLIENT_URL)
    info = client.getblockstats(high)
    data = ''
    for key, item in info.items():
        data += str(key) + ' : ' + str(item).replace('{', '').replace('}', '').replace("'", '').replace(',', ', ').title()+'\n'
    sg.popup(data, title='Statistics about block in the chain')

def exchange_rates():
    ticker = exchangerates.get_ticker()
    d = {}
    for k in ticker:
        d[k] = ticker[k].p15min

    output_peer_string = ''
    for key, item in d.items():
        output_peer_string += str(key) + ' : ' + str(item).replace('{', '').replace('}', '').replace("'", '').replace(',', ', ').title()+'\n'
    sg.popup(output_peer_string, title='Exchange rates')


def Thistory(adresa):
    
    h = history(adresa)
    output_peer_string = ''
    
    dic={}                            
    for index, value in enumerate(h):  
        dic[index] = value             
    for key, item in dic.items():
        output_peer_string += str(key) + ' : ' + str(item).replace('{', '').replace('}', '').replace("'", '').replace(',', ', ').title()+'\n'
    sg.popup(output_peer_string,title='Transaction history')
    

def publkey():

    my_public_key=privtopub(random_key())

    sg.popup(my_public_key,title='Public key')
    
def addr():
    
    my_public_key=privtopub(random_key())
    my_bitcoin_address=pubtoaddr(my_public_key)
    
    sg.popup(my_bitcoin_address,title='Address')
    
    
def main():

    window = sg.Window('Blockchain', layout(), size=(800,500))

    while True:
        event, values = window.read()
        
        if event in (None, 'Cancel'):  # if user closes window
            break
        if event == 'statistic':
            transactions_statistic()
        if event == 'Get statistic':
            block_statistic(int(values['high']))       
        if event == 'private_key':
            sg.popup(random_key(), title='New private key')
        if event == 'rates':
            exchange_rates()
        if event == 'history':
            Thistory(values['adresa'])
        if event == 'public_key':
            publkey()
        if event == 'address':
            addr()

    window.close()

if __name__ == '__main__':
    main()
