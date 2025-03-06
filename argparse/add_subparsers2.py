#设置默认函数
import argparse

parser = argparse.ArgumentParser(prog = 'PROG')
subparsers = parser.add_subparsers(help = 'sub-command help')
def to_string(args):
    print(args.__dict__)
# 添加子命令add
parser_a = subparsers.add_parser('xiaoheilv',help = 'add help')
parser_a.add_argument('-runSpeed',default=1,type = int,help = 'x value')
parser_a.add_argument('-fur',default=2,type = int,help = 'y value')
parser_a.set_defaults(func = to_string)
# 添加命令sub
parser_s = subparsers.add_parser('daheilv',help = 'sub help')
parser_s.add_argument('-speakerSpeed',default=4,type = int,help = 'x value')
parser_s.add_argument('-fur',default=5,type = int,help = 'y value')
parser_s.set_defaults(func=to_string)
args = parser.parse_args()
args.func(args)

#執行
python Test_args.py daheilv -speakerSpeed 30 -fur 2

#結果:
{‘speakerSpeed’: 30, ‘fur’: 2, ‘func’: <function to_string at 0x00000279DC3DDF78>}
