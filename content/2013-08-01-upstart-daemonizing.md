Title: Daemonizing with Upstart
Date: 2013-08-01
Category: System
Tags: upstart, daemon, automation
Slug: upstart-daemonizing
Author: Bing Xia
Summary: Figured out how to daemonize ipython notebook and emacs daemon using upstart

Recently I've been trying to use IPython notebooks more while doing
research. Since the notebook server needs to be started before you can
use the awesomeness of IPython notebooks, I decided to try to find a
method to automatically start my notebook server when I login.

Since I do most of my development on Ubuntu, one obvious choice was
[Upstart](http://upstart.ubuntu.com/). The 'Getting Started' page
pointed me to the [cookbook](http://upstart.ubuntu.com/cookbook/),
which I read through. I found the cookbook to be less of a cookbook,
and more of a comprehensive reference for all the commands, which made
it a little hard to get started. One thing that wasn't explained in
the cookbook was how to enable session init management. However, I
found a helpful page
[here](http://ifdeflinux.blogspot.com/2013/04/upstart-user-sessions-in-ubuntu-raring.html)
which explained how to enable Upstart user sessions.

After some experimentation, I was able to get the following conf file
working:

    :::bash
    # Job configuration for IPython Notebook
    description "IPython Notebook"

    stop on runlevel[06]

    respawn
    respawn limit 10 5 # respawn up to 10 times, waiting 5 seconds each time

    pre-start script
        [ ! -f $HOME/.virtualenvs/molpy3/bin/activate ] && { stop; exit 0; }

        . $HOME/.virtualenvs/molpy3/bin/activate
    end script

    exec $HOME/.virtualenvs/molpy3/bin/ipython3 notebook --profile=nbserver

This file should be placed in `$HOME/.config/upstart` with a `.conf`
extension.

While I was playing with Upstart, I also decided to daemonize my
emacs. I already use `emacs --daemon` on my machine almost
exclusively, but it would be nice for the emacs server to start
automatically and be killed in a nice manner (saving unsaved files) on
shutdown. The script for daemonizing emacs looks very similar, except
that I have a `pre-stop` block which uses emacsclient to call
`(save-some-buffers t)` before emacs is killed.
