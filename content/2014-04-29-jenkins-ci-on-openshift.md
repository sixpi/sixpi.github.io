Title: Jenkins CI on Openshift
Date: 2014-04-29
Tags: automatic, CI
Category: Misc
Slug: jenkins-ci-on-openshift
Author: Bing Xia
Summary: How to set up a free Jenkins build server on Openshift.

In this post, I'll describe how I set up a
[Jenkins CI](https://jenkins-ci.org/) server on
[Openshift](https://www.openshift.com/). This will give you a
continuous integration server which you have (almost) full control
over, for free :).

Openshift is a cloud computing offering by Red Hat, and they helpfully
provides a pre-configured Jenkins application, which we will be
using. After starting the new application process, you can choose from
a number of "Instant Applications", which come ready to go. Just
choose Jenkins Server from the list of instant apps, give your
application a name (I called my "jenkins"), and wait for a little
bit...and your application is created (make sure to note the username
and password). Just point your browser to the provided URL and you
should see your Jenkins app running happily :).

After logging into Jenkins, there are a few things that you'll want to
configure right away. By default, there are no executors to run your
builds, so you'll probably want to set this to 1 (if you're on a free
account and only have access to small gears). You may also want to
configure add a new user with an API key if you want to trigger builds
from other services (such as Bitbucket or Github). Also, many of the
plugins (and Jenkins itself) are older versions, so update them if you
want (if you don't see any updates, go to the advanced tab and click
the "Check Now" button in the lower right).

#### Bitbucket integration

The next thing I wanted to do was enable my Jenkins instance to
automatically build a project from Bitbucket whenever anyone pushed to
it. While creating a new job in Jenkins, check the "Trigger builds
remotely" checkbox. You'll need to create a authentication token (use
a random password generator). Then, from Bitbucket, add a hook to the
project you want to be automatically built. There is a Jenkins hook
you can use - enter the base Jenkins URL, the job name from Jenkins,
and the authentication token. This would normally be all you need to
do to get everything working.

However, there is a little more to be done since the Openshift doens't
give you write access to the home directory. Because of this, SSH
can't save the host key for the Bitbucket servers into
`.ssh/known_hosts`. You can get around this by making a wrapper for
ssh that `git` uses, as described
[here](https://www.openshift.com/forums/openshift/private-git-repo-clone-on-deploy). I
added the extra option `-o
UserKnownHostsFile=$HOME/.openshift_ssh/known_hosts` to also work
around not being able to write to the usual known hosts file. You can
make git always use your ssh wrapper with the command `rhc env set
GIT_SSH=<PATH_TO_SSH_WRAPPER> --app <YOUR_APP_NAME>`.

After these steps, your Jenkins instance should be able to pull from
any git repository you have access to on Bitbucket, even if its a
private repository!
