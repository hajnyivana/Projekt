from bitcoinrpc.authproxy import AuthServiceProxy
import PySimpleGUI as sg

def main():
    CLIENT_URL= 'http://student:WYVyF5DTERJASAiIiYGg4UkRH@blockchain.oss.unist.hr:8332'

    client=AuthServiceProxy(CLIENT_URL)
    info= client.getchaintxstats()

    data = ''
    for key, item in info.items():
        data += str(key) + ' : ' + str(item).replace('{','').replace('}','').replace("'",'').replace(',',', ').title()+'\n'
    
    sg.popup(data,title='Statistics about transactions in the chain')
   
if __name__=='__main__':
    main()