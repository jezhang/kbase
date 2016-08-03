Basic SVN Commands
==================

## Introduction
The help function of Subversion (svn help) provides a summary of the available commands. More detailed information is available from the Subversion on-line book available at http://svnbook.red-bean.com/en/1.2/index.html. Chapter 3 is especially helpful.

The following is a basic set of commands which all editors will use frequently. Some commands have two forms, the long and the short. Both are listed in the description.

### svn checkout/co

svn checkout or svn co. This command is used to pull an SVN tree such as svn://linuxfromscratch.org/BLFS/trunk/BOOK (the BLFS Development book) from the server. You should only need to do this once. If the directory structure is changed (as is sometimes necessary), you may occasionally need to delete your local sand box and re-check it out. If this is going to be needed, it will usually be because the Editor will have made a large change and it will be announced at least on the BLFS-Book mailing list.

### svn add

svn add. When you are creating a new file or directory, you need to tell the SVN server about it. This command does that. Note that the file won't appear in the repository until you do an svn commit (see below).

### svn propset

svn propset. When you are creating a new file or directory, you generally need to tell the SVN to apply properties to the file in places that have keywords in a special format such as $Date: 2012-07-29 17:46:27 -0600 (Sun, 29 Jul 2012) $. Note that the keyword value won't appear in the file until you do an svn commit (see below).

Normally, the command you want is

```sh
svn propset svn:keywords "Date LastChangedBy" /path/to/filename.xml
```

### svn delete

svn delete. This does what it says! When you do an svn commit the file will be deleted from your local sand box immediately as well as from the repository after committing.

### svn status

svn status. This command prints the status of working directories and files. If you have made local changes, it'll show your locally modified items. If you use the --verbose switch, it will show revision information on every item. With the --show-updates (-u) switch, it will show any server out-of-date information.

You should always do a manual svn status --show-updates before trying to commit changes in order to check that everything is OK and ready to go.

### svn update/up

svn update or svn up. This command syncs your local sand box with the server. If you have made local changes, it will try and merge any changes on the server with your changes on your machine.

### svn commit/ci

svn commit or svn ci. This command recursively sends your changes to the SVN server. It will commit changed files, added files, and deleted files. Note that you can commit a change to an individual file or changes to files in a specific directory path by adding the name of the file/directory to the end of the command. The -m option should always be used to pass a log message to the command. Please don't use empty log messages (see later in this document the policy which governs the log messages).

### svn diff

svn diff. This is useful for two different purposes. First, those without write access to the BLFS SVN server can use it to generate patches to send to the BLFS-Dev mailing list. To do this, simply edit the files in your local sand box then run svn diff > FILE.patch from the root of your BLFS directory. You can then attach this file to a message to the BLFS-Dev mailing list where someone with editing rights can pick it up and apply it to the book. The second use is to find out what has changed between two revisions using: svn diff -r revision1:revision2 FILENAME. For example: svn diff -r 168:169 index.xml will output a diff showing the changes between revisions 168 and 169 of index.xml.

### svn move

svn move SRC DEST or svn mv SRC DEST or svn rename SRC DEST or svn ren SRC DEST. This command moves a file from one directory to another or renames a file. The file will be moved on your local sand box immediately as well as on the repository after committing.