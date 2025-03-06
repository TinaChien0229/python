#Test_args.py :
import argparse

parser = argparse.ArgumentParser(prog = 'PROG')
subparsers = parser.add_subparsers(help = 'sub-command help')
# 添加子命令add
parser_a = subparsers.add_parser('xiaoheilv',help = 'animal xiaoheilv')
parser_a.add_argument('-runSpeed',default=1,type = int,help = 'x value')
parser_a.add_argument('-fur',default=2,type = int,help = 'y value')
# 添加命令sub
parser_s = subparsers.add_parser('daheilv',help = 'animal daheilv')
parser_s.add_argument('-speakerSpeed',default=4,type = int,help = 'x value')
parser_s.add_argument('-fur',default=5,type = int,help = 'y value')

args = parser.parse_args()
print(args)

#執行:
python Test_args.py xiaoheilv -runSpeed 30 -fur 2

#結果:
Namespace(fur=2, runSpeed=30)

#執行:
python Test_args.py daheilv -speakerSpeed 30 -fur 2

#結果:
Namespace(fur=2, speakerSpeed=30)
