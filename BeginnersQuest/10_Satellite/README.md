<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">Satellite</h1>
<h1 class="glitch glitch__color glitch__color--green">Satellite</h1>
<h1 class="glitch glitch__color glitch__color--blue">Satellite</h1>
<h1 class="glitch glitch__color">Satellite</h1>
<br />
<br />


## Task

Placing your ship in range of the Osmiums, you begin to receive signals. Hoping that you are not detected, because it's too late now, you figure that it may be worth finding out what these signals mean and what information might be "borrowed" from them. Can you hear me Captain Tim? Floating in your tin can there? Your tin can has a wire to ground control?

Find something to do that isn't staring at the Blue Planet.

[Attachment](https://storage.googleapis.com/gctf-2019-attachments/768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf)

## Solution
Inspecting the README.pdf reveals the satellite name: `osmium`
The link in the console output doesn't lead to a flag..
The binary doesn't contain any strings related to the output, so it maybe fetches data from the internet
Sniffing the network traffic of the application and filtering by the ipaddress 34.76.101.29 reveals the message in cleartext containing the [flag](./flags.html#10_satellite):
