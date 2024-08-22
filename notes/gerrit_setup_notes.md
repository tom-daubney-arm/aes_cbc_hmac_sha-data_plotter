# How to set up Gerrit

## Generating a new SSH Key
You need to generate an SSH key and export it to Gerrit in order for your SSH requests to be accepted.
To do this, open a terminal and enter the following command, substiting your own email:

`ssh-keygen -t ed25519 -C "your_email@example.com"`

This generates a new SSH key and uses the provided email as the label. You will be promted to create a file name for the key file, or you can accept the default. You will also be prompted to enter a passphrase to protect the key files but you can simpy press <enter> in order to not set a passphrase.

## Exporting the key to Gerrit
Once the key is generated you should be left with two files in your `.ssh` directory which is usually located at:
`/home/<user_name>/.ssh/`

The files will be called whatever you named them in the step above, the difference between the two being that one has a `.pub` extension indicating that it contains the public key, where as the one with an extension will contain the private key. If you did not change the suggested file name when generating the key then the two files are likely called:

`/home/<user_name>/.ssh/id_ed25519` and `/home/<user_name>/.ssh/id_ed25519.pub`

The contents of the public key file is what is needed to be uploaded to Gerrit. The private key must never be shared.

To export the key to Gerrit, head over to:
`https://gerrit.oss.arm.com/settings/ssh-keys#SSHKeys`
and copy and paste the contents of the `.pub` file you created above into the text box labeled `New SSH Key`. The contents of the `.pub` file should look like:
`ssh-ed25519 <Public key strin> <your.email@arm.com>`

Once you have pasted the `.pub` file contents into the box, a button labeled `ADD NEW SSH KEY` will become active. Click it and you will see your key added to the list of keys.

## Add the key to the SSH Agent
This means that you won't have to enter the SSH key so often.
`eval "$(ssh-agent -s)"`
`ssh-add /path/to/your/private/ssh/key`


At this point you should be ready to use Gerrit with SSH.
