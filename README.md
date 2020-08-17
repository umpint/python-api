# umpint.com - Python Example API

Python API example to umpint.com document signing service.
This could be used in production as is reasonable fast.
But also can be used as sample code to embedd in you own application

## Getting Started

Just clone this project. Then can run the sign.py to sign just one document. Or use the batch-sign.py to sign every document in a directory. The batch-sign.sh is much faster as will only send one request to our server with all the request contained in it.

### Prerequisites

These scripts should work on any standard Python3 installation. Only relies on:
1) base64
2) Crypto
3) sys
4) os
5) urllib

As long as these are installed on your host these scripts should work.

Only other requirements are that you need access to umpint.com over the internet to send the data. And you need access to the private key of the certificate of the domain you want to sign for.

### Installing

```
git clone https://github.com/umpint/python-api.git
cd python-api
```

### Running

We have at dummybank.co.uk a dummy site you can use for testing. Since we only use if for testing we allow you to download the Certificate Private Key. Nobody should normally every allow this - as makes https pointless.

You can download from: dummybank.co.uk/notnormallpublic/privkey.pem 

Note this file changes every few months so you may have to download again if you start getting certificate errors.

Place this file in the bash-api directory.

To sign an individual file run:
```
wget https://dummybank.co.uk/notnormallpublic/privkey.pem
# 1st edit the file testfile.sh and make random change to it so it is unique
./sign.py dummybank.co.uk ./key.pem testfile.txt
```

you should then see output like this:

```
Args passed:['./sign.py', 'dummybank.co.uk', './privkey.pem', 'testfile.txt']
hash String:6ddb25c37e4851709a9116f8357673010dd12c05eb2ac4cc9a2f682ae8d4f8b2
Signature:L4fyqF07vchmiVe8xIqJ6NmJP4a4gVUsC0bIO7t8jYdDC6gjGOWxz0fHlDP6t5hjdog2H4b/1k/j/y34UUhanwnmehmPq0HL9QYDVFU3e4VRm3xdosm8PtVdM+XUkFtJ8FW23/7kcv5faSEKGdMSygRjT841XJ+VXnoeSkg2m9kGhQsM5KEtYqUQvqT1vLi7zKIuHkKb86a6V7sP7YSBOHV/rVx4koPLoMbUw+ZPlbsrtbpm3+fQPv9Anm/43U5SLvLEhrnhqavMIOauzl2/Whjg65mt6RysrpZXGETlyb1EmJprL1xB5d7uzzE/CdgdywxYyq1SDDh4hiOwjBGP7g==
b'signed OK dummybank.co.uk 6ddb25c37e4851709a9116f8357673010dd12c05eb2ac4cc9a2f682ae8d4f8b2 L4fyqF07vchmiVe8xIqJ6NmJP4a4gVUsC0bIO7t8jYdDC6gjGOWxz0fHlDP6t5hjdog2H4b/1k/j/y34UUhanwnmehmPq0HL9QYDVFU3e4VRm3xdosm8PtVdM+XUkFtJ8FW23/7kcv5faSEKGdMSygRjT841XJ+VXnoeSkg2m9kGhQsM5KEtYqUQvqT1vLi7zKIuHkKb86a6V7sP7YSBOHV/rVx4koPLoMbUw+ZPlbsrtbpm3+fQPv9Anm/43U5SLvLEhrnhqavMIOauzl2/Whjg65mt6RysrpZXGETlyb1EmJprL1xB5d7uzzE/CdgdywxYyq1SDDh4hiOwjBGP7g=='
```

The "signed OK" signifies that the signature was correct and it was a new file.

If instead you see "duplicate already in db" this just means that you probably did not change the "testfile.txt" or have upload the file twice and so we already had a signature in the database. To fix this issue just change the file in some way.

The batch_sign.py is used in exactly the same way. Only difference is that the last perameter is the path to a directory. And all the files will be signed in one call to the umpint.com API. Also results will be returned as a JSON array - see: https://github.com/umpint/rest-api/blob/master/batch_sign.md


## Contributing

Please just create a pull request and we will review and merge.

## Authors

* **Robin Owens** - *Initial work* - [umpint](https://github.com/umpint)

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE-2.0.txt](LICENSE-2.0.txt) file for details

## Acknowledgments

* People who wrote OpenSSL!
