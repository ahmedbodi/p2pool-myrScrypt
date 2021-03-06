from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    bitcoin=math.Object(
        PARENT=networks.nets['bitcoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='fc70035c7a81bc6f'.decode('hex'),
        PREFIX='2472ef181efcd37b'.decode('hex'),
        P2P_PORT=9333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=9332,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st portals94.ns01.us 54.227.25.14 119.1.96.99 204.10.105.113 76.104.150.248 89.71.151.9 76.114.13.54 72.201.24.106 79.160.2.128 207.244.175.195 168.7.116.243 94.23.215.27 218.54.45.177 5.9.157.150 78.155.217.76 91.154.90.163 173.52.43.124 78.225.49.209 220.135.57.230 169.237.101.193:8335 98.236.74.28 204.19.23.19 98.122.165.84:8338 71.90.88.222 67.168.132.228 193.6.148.18 80.218.174.253 50.43.56.102 68.13.4.106 24.246.31.2 176.31.208.222 1.202.128.218 86.155.135.31 204.237.15.51 5.12.158.126:38007 202.60.68.242 94.19.53.147 65.130.126.82 184.56.21.182 213.112.114.73 218.242.51.246 86.173.200.160 204.15.85.157 37.59.15.50 62.217.124.203 80.87.240.47 198.61.137.12 108.161.134.32 198.154.60.183:10333 71.39.52.34:9335 46.23.72.52:9343 83.143.42.177 192.95.61.149 144.76.17.34 46.65.68.119 188.227.176.66:9336 75.142.155.245:9336 213.67.135.99 76.115.224.177 50.148.193.245 64.53.185.79 80.65.30.137 109.126.14.42 76.84.63.146'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
        VERSION_WARNING=lambda v: 'Upgrade Bitcoin to >=0.8.5!' if v < 80500 else None,
    ),
    bitcoin_testnet=math.Object(
        PARENT=networks.nets['bitcoin_testnet'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='5fc2be2d4f0d6bfb'.decode('hex'),
        PREFIX='3f6057a15036f441'.decode('hex'),
        P2P_PORT=19333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19332,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st liteco.in'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
    ),

    litecoin=math.Object(
        PARENT=networks.nets['litecoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='e037d5b8c6923410'.decode('hex'),
        PREFIX='7208c1a53ef629b0'.decode('hex'),
        P2P_PORT=9338,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9327,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st liteco.in 95.211.21.103 37.229.117.57 66.228.48.21 180.169.60.179 112.84.181.102 74.214.62.115 209.141.46.154 78.27.191.182 66.187.70.88 88.190.223.96 78.47.242.59 158.182.39.43 180.177.114.80 216.230.232.35 94.231.56.87 62.38.194.17 82.67.167.12 183.129.157.220 71.19.240.182 216.177.81.88 109.106.0.130 113.10.168.210 218.22.102.12 85.69.35.7:54396 201.52.162.167 95.66.173.110:8331 109.65.171.93 95.243.237.90 208.68.17.67 87.103.197.163 101.1.25.211 144.76.17.34 209.99.52.72 198.23.245.250 46.151.21.226 66.43.209.193 59.127.188.231 178.194.42.169 85.10.35.90 110.175.53.212 98.232.129.196 116.228.192.46 94.251.42.75 195.216.115.94 24.49.138.81 61.158.7.36 213.168.187.27 37.59.10.166 72.44.88.49 98.221.44.200 178.19.104.251 87.198.219.221 85.237.59.130:9310 218.16.251.86 151.236.11.119 94.23.215.27 60.190.203.228 176.31.208.222 46.163.105.201 198.84.186.74 199.175.50.102 188.142.102.15 202.191.108.46 125.65.108.19 15.185.107.232 108.161.131.248 188.116.33.39 78.142.148.62 69.42.217.130 213.110.14.23 185.10.51.18 74.71.113.207 77.89.41.253 69.171.153.219 58.210.42.10 174.107.165.198 50.53.105.6 116.213.73.50 83.150.90.211 210.28.136.11 86.58.41.122 70.63.34.88 78.155.217.76 68.193.128.182 198.199.73.40 193.6.148.18 188.177.188.189 83.109.6.82 204.10.105.113 64.91.214.180 46.4.74.44 98.234.11.149 71.189.207.226'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-ltc',
        VERSION_CHECK=lambda v: True,
        VERSION_WARNING=lambda v: 'Upgrade Litecoin to >=0.8.5.1!' if v < 80501 else None,
    ),
    terracoin=math.Object(
        PARENT=networks.nets['terracoin'],
        SHARE_PERIOD=30, # seconds
        NEW_SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//30, # shares
        REAL_CHAIN_LENGTH=24*60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        NEW_SPREAD=15, # blocks
        IDENTIFIER='a41b2356a1b7d35e'.decode('hex'),
        PREFIX='5623b62178d2b8a3'.decode('hex'),
        P2P_PORT=9323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=9322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st 93.97.192.93 66.90.73.83 67.83.108.0 219.84.64.174 24.167.17.248 109.74.195.142 83.211.86.49 94.23.34.145 168.7.116.243 94.174.40.189:9344 89.79.79.195 portals94.ns01.us'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    terracoin_testnet=math.Object(
        PARENT=networks.nets['terracoin_testnet'],
        SHARE_PERIOD=30, # seconds
        NEW_SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//30, # shares
        REAL_CHAIN_LENGTH=60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        NEW_SPREAD=15, # blocks
        IDENTIFIER='b41b2356a5b7d35d'.decode('hex'),
        PREFIX='1623b92172d2b8a2'.decode('hex'),
        P2P_PORT=19323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),

    digitalcoin=math.Object(
        PARENT=networks.nets['digitalcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=45, # blocks
        IDENTIFIER='797EC5BC40AFA22E'.decode('hex'),
        PREFIX='23CD74AF85036A9F'.decode('hex'),
        P2P_PORT=23610,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8810,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    
    worldcoin=math.Object(
        PARENT=networks.nets['worldcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=60, # blocks
        IDENTIFIER='5AE1DD1E84E6EC3A'.decode('hex'),
        PREFIX='43B80223C931E0A0'.decode('hex'),
        P2P_PORT=23620,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8820,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    
    craftcoin=math.Object(
        PARENT=networks.nets['craftcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='755F8AD0DD49380A'.decode('hex'),
        PREFIX='31357EF0ECB3C1BC'.decode('hex'),
        P2P_PORT=23630,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8830,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    casinocoin=math.Object(
        PARENT=networks.nets['casinocoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=60, # blocks
        IDENTIFIER='5AE1F9AAEA359544'.decode('hex'),
        PREFIX='43DC544D48689C0D'.decode('hex'),
        P2P_PORT=23640,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8840,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com bigiron.homelinux.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    anoncoin=math.Object(
        PARENT=networks.nets['anoncoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=10, # blocks
        IDENTIFIER='40C08900F98B2AFA'.decode('hex'),
        PREFIX='43F8D4260E9F8E60'.decode('hex'),
        P2P_PORT=23650,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8850,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com anc.ottrbutt.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),

    bbqcoin=math.Object(
        PARENT=networks.nets['bbqcoin'],
        SHARE_PERIOD=10, # seconds
        NEW_SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='626974636f696e21'.decode('hex'),
        PREFIX='6772696c6c697421'.decode('hex'),
        P2P_PORT=12339,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8900,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com alduin.cubox.me 174.58.242.26 bbq.crabdance.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    franko=math.Object(
        PARENT=networks.nets['franko'],
        SHARE_PERIOD=15, # seconds target spacing
        NEW_SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='be43F5b8c6924210'.decode('hex'),
        PREFIX='b587192ba6d4729a'.decode('hex'),
        P2P_PORT=9798,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9797,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ), 
    dogecoin=math.Object(
        PARENT=networks.nets['dogecoin'],
	      SHARE_PERIOD=15, # seconds target spacing
        NEW_SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=12*60*60//15, # shares
        REAL_CHAIN_LENGTH=12*60*60//15, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=10, # blocks
	      NEW_SPREAD=10, # blocks
        IDENTIFIER='D0D1D2D3B2F68CD9'.decode('hex'),
        PREFIX='D0D3D4D541C11DD9'.decode('hex'),
        P2P_PORT=8555,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9555,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com doge.dtdns.net pool.hostv.pl rav3n.dtdns.net p2pool.org'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    potcoin=math.Object(
            PARENT=networks.nets['potcoin'],
            SHARE_PERIOD=10, # seconds target spacing
            NEW_SHARE_PERIOD=10, # seconds target spacing
            CHAIN_LENGTH=24*60*60//10, # shares
            REAL_CHAIN_LENGTH=24*60*60//10, # shares
            TARGET_LOOKBEHIND=200, # shares coinbase maturity
            SPREAD=10, # blocks
            NEW_SPREAD=10, # blocks
            IDENTIFIER='DDA1A1D3B2F68CDD'.decode('hex'),
            PREFIX='A2C3D4D541C11DDD'.decode('hex'),
            P2P_PORT=8420,
            MIN_TARGET=0,
            MAX_TARGET=2**256//2**20 - 1,
            PERSIST=False,
            WORKER_PORT=9420,
            BOOTSTRAP_ADDRS='us-east1.cryptovein.com'.split(' '),
            ANNOUNCE_CHANNEL='#cryptovein',
            VERSION_CHECK=lambda v: True,
        ),
    mooncoin=math.Object( #565
        PARENT=networks.nets['mooncoin'],
        SHARE_PERIOD=25, # seconds target spacing
	      NEW_SHARE_PERIOD=25, # seconds target spacing
        CHAIN_LENGTH=12*60*60//25, # shares
        REAL_CHAIN_LENGTH=12*60*60//25, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=10, # blocks
	      NEW_SPREAD=10, # blocks
        IDENTIFIER='e8e8c0c0f7f7f9f9'.decode('hex'),
        PREFIX='c0c0e8e8f7f7f9f9'.decode('hex'),
        P2P_PORT=8664,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9664,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
     globalcoin=math.Object(
        PARENT=networks.nets['globalcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=45, # blocks
        IDENTIFIER='5F0183D62F698832'.decode('hex'),
        PREFIX='52F8CF5955E02234'.decode('hex'),
        P2P_PORT=23660,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8860,
        BOOTSTRAP_ADDRS='xpool.net us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    feathercoin=math.Object(
        PARENT=networks.nets['feathercoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=120, # blocks
        IDENTIFIER='4665617468657221'.decode('hex'),
        PREFIX='b131010ba6d4729a'.decode('hex'),
        P2P_PORT=19339,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com pool.maeh.org pool2.maeh.org'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    smartcoin=math.Object(
        PARENT=networks.nets['smartcoin'],
        SHARE_PERIOD=5, # seconds
        CHAIN_LENGTH=12*60*60//5, # shares
        REAL_CHAIN_LENGTH=12*60*60//5, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=50, # blocks
        IDENTIFIER='defadefaced0ced0'.decode('hex'),
        PREFIX='d0cededefafac0ce'.decode('hex'),
        P2P_PORT=8585,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9585,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    leafcoin=math.Object(
        PARENT=networks.nets['leafcoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=50, # blocks
        IDENTIFIER='fc656166636f696e'.decode('hex'),
        PREFIX='fe636f696e6c656a'.decode('hex'),
        P2P_PORT=8166,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9166,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org taken.pl'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    flappycoin=math.Object(
        PARENT=networks.nets['flappycoin'],
        SHARE_PERIOD=15,
        CHAIN_LENGTH=12*60*60//15,
        REAL_CHAIN_LENGTH=12*60*60//15,
        TARGET_LOOKBEHIND=20,
        SPREAD=10,
        IDENTIFIER='C0C1C2C3B2F68CD9'.decode('hex'),
        PREFIX='C0C3C4C541C11DD9'.decode('hex'),
        P2P_PORT=65150,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=65050,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com 162.248.163.195 162.219.3.121'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    kittehcoin=math.Object(
        PARENT=networks.nets['kittehcoin'],
        SHARE_PERIOD=5, # seconds
        CHAIN_LENGTH=12*60*60//5, # shares
        REAL_CHAIN_LENGTH=12*60*60//5, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=50, # blocks
        IDENTIFIER='c0c1c2e3e6e9f1ab'.decode('hex'),
        PREFIX='f1c3e9a023e0f078'.decode('hex'),
        P2P_PORT=8566,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9566,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com taken.pl lovok.no-ip.com meow-il.zapto.org p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    nyancoin=math.Object(
        PARENT=networks.nets['nyancoin'],
        SHARE_PERIOD=10, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='5D4D5622297EE0E4'.decode('hex'),
        PREFIX='4DD804B010424A99'.decode('hex'),
        P2P_PORT=23670,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8870,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com xpool.net'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    mincoin=math.Object(
        PARENT=networks.nets['mincoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=15, # blocks
        IDENTIFIER='6031F5b8c6924210'.decode('hex'),
        PREFIX='6290192ba6d4729a'.decode('hex'),
        P2P_PORT=8732,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9773,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    megacoin=math.Object(
        PARENT=networks.nets['megacoin'],
        SHARE_PERIOD=5, # seconds target spacing
        NEW_SHARE_PERIOD=5, # seconds target spacing
        CHAIN_LENGTH=3*60*60//10, # shares
        REAL_CHAIN_LENGTH=3*60*60//10, # shares
        TARGET_LOOKBEHIND=20, # shares coinbase maturity
        SPREAD=10, # blocks
        NEW_SPREAD=10, # blocks
        IDENTIFIER='D0D1D2D3B2F68CDD'.decode('hex'),
        PREFIX='D0D3D4D541C11DDD'.decode('hex'),
        P2P_PORT=8556,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9556,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    cannacoin=math.Object(
        PARENT=networks.nets['cannacoin'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='ea21a7b8c322482f'.decode('hex'),
        PREFIX='e280193ce6a4927c'.decode('hex'),
        P2P_PORT=7742,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=7743,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    goldcoin=math.Object(
        PARENT=networks.nets['goldcoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=20, # shares
        SPREAD=50, # blocks
        IDENTIFIER='673C4A194010994F'.decode('hex'),
        PREFIX='673C4A1922156F1F'.decode('hex'),
        P2P_PORT=23220,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=8221,
        BOOTSTRAP_ADDRS='us-east1.cryptovein.com 63.170.87.173 inetrader.com'.split(' '),
        ANNOUNCE_CHANNEL='#cryptovein',
        VERSION_CHECK=lambda v: True,
    ),
    myriad_scrypt=math.Object(
        PARENT=networks.nets['myriad_scrypt'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=60, # blocks
        IDENTIFIER='fafa54457667eeee'.decode('hex'),
        PREFIX='fa6754ee45ee76fa'.decode('hex'),
        P2P_PORT=5555,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=5556,
        BOOTSTRAP_ADDRS='birdspool.no-ip.org'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),



)
for net_name, net in nets.iteritems():
    net.NAME = net_name
