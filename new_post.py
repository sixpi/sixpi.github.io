import sys, os, datetime, re, subprocess

# get content folder from command line
input_dir = sys.argv[1]
today = datetime.datetime.now().strftime("%Y-%m-%d")

# prompt user for post title
post_title = raw_input('ENTER POST TITLE: ')
post_title_slug = re.sub(r'[^a-zA-Z0-9\.]+', '-', post_title).lower()

metadata = """Title: %s
Date: %s
Tags:
Category: Misc
Slug: %s
Author: Bing Xia
Summary:
""" % (post_title, today, post_title_slug)


# open file and write metadata
filepath = input_dir + '/' + post_title_slug + '.md'
subprocess.call(['touch', filepath])

f = open(filepath, 'r+b')
f.write(metadata)
f.close()

if f:
    print '\n'
    print 'NEW POST CREATED: %s' %(filepath)
