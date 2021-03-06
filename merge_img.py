# -*- coding: utf-8 -*-
"""
图片合并加注释的工具类

Author: liyan
File: merge_img.py

Features:
1. 把多张图片合并为一张垂直依次排列的大图
2. 大图带标题，小图带编号和注释
3. 合并后的图片：vertical.png
"""

import argparse
from util import Command

def test():
	"""
	"""
	my_labels = 'first step; second step; third step; forth step'.split(';')
	try:
		print 'begin merge...'
		Command.merge_img(src_img='j_[1-4].jpg', width=300, caption='做一个测试', labels=my_labels, clean=False)
		print 'merge over.'
	except Exception, e: 
		print 'except:', e
		raise


def main():
	parser = argparse.ArgumentParser(description='Xcode Builder.')
	parser.add_argument('-a', dest='action', type=str, default='merge', choices=('test', 'merge'), 
											help='Action perform')
	parser.add_argument('-t', dest='img_type', type=str, default='jpg',
											help='image type')
	parser.add_argument('-n', dest='img_name', type=str, default='',
											help='image name: <img_name>_[1-9].<img_type> <img_name>_[1-9][0-9].<img_type>')
	parser.add_argument('-w', dest='img_width', type=int, default=720,
											help='Width of the merge image')
	parser.add_argument('-c', dest='caption', type=str, default='标题： 这是一个测试',
											help='image caption')
	parser.add_argument('-l', dest='labels', type=str, default='l1;l2;l3;l4',
											help='label for eath image, split by ;')
	parser.add_argument('--clean', dest='clean', action='store_false',
											help='Remove working files')
	parser.set_defaults(clean=True)
	

	args = parser.parse_args()

	img_pattern = '%(img_name)s_[0-9].%(img_type)s %(img_name)s_[1-9][0-9].%(img_type)s' % {
					'img_name': args.img_name,
					'img_type': args.img_type
				}
	print 'img_pattern=', img_pattern
	# test()
	index = 1
	for lable in args.labels.split(';'):
		print index, lable
		index = index + 1
	# for f in *.jpg; do mv $f g_${f} ; done
	# python /opt/local/ide/git_storage/github/ci_scripts/merge_img.py -n g -c "caption of these images" -l "1;2;3..split by ;" --clean
	Command.merge_img(src_img=img_pattern, width=args.img_width, caption=args.caption, labels=args.labels.split(';'), clean=args.clean)
	


if __name__ == '__main__':
	main()