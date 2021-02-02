#lgtm/core.py
import click
@click.command()
@click.option('--message', '-m', default='LGTM', show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli():
	"""LGTM画像生成ツール"""
	lgtm()
	click.echo('lgtm') #動作確認用
	

def lgtm(keyword, message):
	#ここにロジックを追加していく
	pass
