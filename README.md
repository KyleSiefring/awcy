Are We Compressed Yet?
====
This repository contains the arewecompressedyet.com website source code.

Running your own local copy of the website
===
To run a local copy, you will need to install node.js on your computer, create a configuration
file called `config.json`, and a `secret_key` file which houses a password. The configuration
file contains only one setting right now, which is the IRC channel that the AWCY bot will join. The
password allows run submission to awcy. Awcy will run with any password.

Here is an example config.json:

```
{ "channel": "#daalatest",
  "have_aws": false,
  "port": 3000
}
```

These commands will create the configuration files and install the node.js modules that get used by
awcy. Open a node command line and run the following:

```
echo 'fake_password_to_compile' > secret_key
npm install
npm start
```

To run the server, execute the run_awcy.bat file
or run the following in your command line:
```
  node awcy_server.js
```
Now you can open localhost:3000 with your browser to see your local version of the website.

Run database format
===
The runs/ directory will contain all of the output files generated from a job. There is a info.json file that specifies what options were used by that particular run. Here is an example of an info.json file:

  {"codec":"daala","commit":"","run_id":"2014-09-19T22-00-08.196Z","task":"video-1-short","nick":"AWCY","task_type":"video"}

There is also an output.txt file that contains the output of the rd_tool.py script.

After each run, a cache file called list.json file is generated by the generate_list.js script. This contains all of the info.json files, as an ordered list. This should probably be replaced by a "real" database at some point.
