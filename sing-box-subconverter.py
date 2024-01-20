import json
import argparse

from singbox_subscribe.parsers import clash2base64 as __clash2base64
from singbox_subscribe.parsers import http as __http
from singbox_subscribe.parsers import https as __https
from singbox_subscribe.parsers import hysteria as __hysteria
from singbox_subscribe.parsers import hysteria2 as __hysteria2
from singbox_subscribe.parsers import socks as __socks
from singbox_subscribe.parsers import ss as __ss
from singbox_subscribe.parsers import ssr as __ssr
from singbox_subscribe.parsers import trojan as __trojan
from singbox_subscribe.parsers import tuic as __tuic
from singbox_subscribe.parsers import vless as __vless
from singbox_subscribe.parsers import vmess as __vmess
from singbox_subscribe.parsers import wg as __wg

from singbox_subscribe import main as M


def get_parsers():
    parsers_mod = {}
    parsers_mod['clash2base64'] = __clash2base64
    parsers_mod['http'] = __http
    parsers_mod['https'] = __https
    parsers_mod['hysteria'] = __hysteria
    parsers_mod['hysteria2'] = __hysteria2
    parsers_mod['socks'] = __socks
    parsers_mod['ss'] = __ss
    parsers_mod['ssr'] = __ssr
    parsers_mod['trojan'] = __trojan
    parsers_mod['tuic'] = __tuic
    parsers_mod['vless'] = __vless
    parsers_mod['vmess'] = __vmess
    parsers_mod['wg'] = __wg
    return parsers_mod


VERSION = '1.0.6'


def main(args):
    M.parsers_mod = get_parsers()
    M.providers = {
        'subscribes': [
            {
                'enabled': True,
                'url': args.url or args.path,
                'User-Agent': args.ua or 'clashmeta'
            }
        ]
    }

    nodes = None
    if args.url:
        nodes = M.get_nodes(args.url)
    elif args.path:
        nodes = M.get_nodes(args.path)
    else:
        raise Exception('subscribe url or path not specified')

    if not nodes:
        raise Exception('nodes not found')
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(json.dumps(nodes, indent=2,
                ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help='subscribe url', default=None)
    parser.add_argument('--ua', type=str, help='User Agent', default=None)
    parser.add_argument('--path', type=str,
                        help='subscribe file path', default=None)
    parser.add_argument('--out', type=str,
                        help='output file path', default=None)
    parser.add_argument('--version', action='version', version=VERSION)

    args = parser.parse_args()
    if not args.out:
        raise Exception('output file not specified')
    else:
        main(args=args)
