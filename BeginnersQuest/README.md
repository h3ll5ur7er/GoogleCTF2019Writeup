# Google CTF 2019 Beginners Quest

<!-- <iframe src="/root/ctf/GoogleCTF2019Writeup/BeginnersQuest/map/index.html" width="100%" height="100%"></iframe> -->

<script src="jquery.js"></script>
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="-200 -200 1300 600" width="800" height="300" preserveAspectRatio="xMidYMid meet" xml:space="preserve" >
    <defs>
        <style type="text/css">
            <![CDATA[
                body {
                    background: black;
                }
                svg {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                }
                iframe {
                    border:none;
                    padding:.5em;
                    margin:1.5em 0 1em;
                    width:100%;
                    height:100%;
                }
                .line {
                    stroke: rgb(100, 100, 100);
                    stroke-width: 5;
                }
                .grid {
                    stroke: rgb(55, 55, 55);
                    stroke-width: 1;
                }
                circle {
                    stroke: gray;
                }
                .red {
                    fill: red;
                }
                .green {
                    fill: lime;
                }
                .blue {
                    fill: blue;
                }
                .yellow {
                    fill: yellow;
                }
                .darkgreen {
                    fill: green;
                }
                .gray {
                    fill: lightgray;
                }
                svg {
                    max-width: 100% !important;
                    height: auto;
                    display: block;
                }
                .heyo:hover {
                    -moz-transition: 0.3s;
                    -o-transition: 0.3s;
                    -webkit-transition: 0.3s;
                    transition: 0.3s;
                }
                .enabled {
                    cursor: pointer;
                }
                .description {
                    pointer-events: none;
                    position: absolute;
                    font-size: 18px;
                    text-align: center;
                    background: white;
                    padding: 10px 15px;
                    z-index: 5;
                    height: 30px;
                    line-height: 30px;
                    margin: 0 auto;
                    border-radius: 5px;
                    box-shadow: 0 0 0 1px #eee;
                    -moz-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    -webkit-transform: translateX(-50%);
                    transform: translateX(-50%);
                    display: none;
                }
                .description.active {
                    display: block;
                }
                .description:after {
                    content: "";
                    position: absolute;
                    left: 50%;
                    top: 100%;
                    width: 0;
                    height: 0;
                    margin-left: -10px;
                    border-left: 10px solid transparent;
                    border-right: 10px solid transparent;
                    border-top: 10px solid white;
                }]]>
            </style>
        </defs>
        <line class="grid" x1="0"   y1="-50" x2="0"   y2="350" />
        <line class="grid" x1="100" y1="-50" x2="100" y2="350" />
        <line class="grid" x1="200" y1="-50" x2="200" y2="350" />
        <line class="grid" x1="300" y1="-50" x2="300" y2="350" />
        <line class="grid" x1="400" y1="-50" x2="400" y2="350" />
        <line class="grid" x1="500" y1="-50" x2="500" y2="350" />
        <line class="grid" x1="600" y1="-50" x2="600" y2="350" />
        <line class="grid" x1="700" y1="-50" x2="700" y2="350" />
        <line class="grid" x1="800" y1="-50" x2="800" y2="350" />
        <line class="grid" x1="900" y1="-50" x2="900" y2="350" />
        <line class="grid" x1="-50" y1="0"   x2="950" y2="0"   />
        <line class="grid" x1="-50" y1="100" x2="950" y2="100" />
        <line class="grid" x1="-50" y1="200" x2="950" y2="200" />
        <line class="grid" x1="-50" y1="300" x2="950" y2="300" />
        <line class="line" x1="0"   y1="0"   x2="100" y2="100" />
        <line class="line" x1="100" y1="100" x2="200" y2="200" />
        <line class="line" x1="100" y1="100" x2="200" y2="100" />
        <line class="line" x1="200" y1="100" x2="300" y2="100" />
        <line class="line" x1="200" y1="200" x2="500" y2="200" />
        <line class="line" x1="300" y1="100" x2="400" y2="0"   />
        <line class="line" x1="300" y1="300" x2="500" y2="100" />
        <line class="line" x1="400" y1="0"   x2="500" y2="0"   />
        <line class="line" x1="400" y1="100" x2="500" y2="200" />
        <line class="line" x1="500" y1="100" x2="700" y2="300" />
        <line class="line" x1="500" y1="200" x2="600" y2="100" />
        <line class="line" x1="500" y1="300" x2="600" y2="300" />
        <line class="line" x1="600" y1="100" x2="700" y2="100" />
        <line class="line" x1="700" y1="300" x2="800" y2="200" />
        <line class="line" x1="800" y1="200" x2="900" y2="200" />
        <circle name="Enter Space-Time Coordinates" href="./00_EnterSpaceTimeCoordinates/READMEe.html" class="green enabled heyo" cx="0"   cy="0"   r="8" />
        <circle name="Satellite" href="./10_Satellite/README.html" class="blue enabled heyo" cx="100" cy="100" r="8" />
        <circle name="Home Computer" href="./20_HomeComputer/README.html" class="green enabled heyo" cx="200" cy="100" r="8" />
        <circle name="Work Computer" href="./21_WorkComputer/README.html" class="red enabled heyo" cx="200" cy="200" r="8" />
        <circle name="Government Agricultural Network" href="./30_GovernmentAgriculturalNetwork/README.html" class="yellow enabled heyo" cx="300" cy="100" r="8" />
        <circle name="From 'Work Computer' advanced flag" href="./__default.html" class="red enabled heyo" cx="300" cy="300" r="8" />
        <circle name="STOP GAN" href="./40_StopGAN/README.html" class="red enabled heyo" cx="400" cy="0"   r="8" />
        <circle name="From 'Cookie World Order /?\' advanced flag" href="./__default.html" class="yellow enabled heyo" cx="400" cy="100" r="8" />
        <circle name="Ending 1" href="./__default.html" class="gray enabled heyo" cx="500" cy="0"   r="8" />
        <circle name="Cookie World Order" href="./51_CookieWorldOrder/README.html" class="yellow enabled heyo" cx="500" cy="100" r="8" />
        <circle name="FriendSpaceBookPlusAllAccessRedPremium" href="./52_FriendSpaceBookPlusAllAccessRedPremium/README.html" class="green enabled heyo" cx="500" cy="200" r="8" />
        <circle name="From 'StopGAN' advanced flag" href="./__default.html" class="red enabled heyo" cx="500" cy="300" r="8" />
        <circle name="Drive To Target" href="./60_DriveToTarget/README.html" class="blue enabled heyo" cx="600" cy="100" r="8" />
        <circle name="Ending 2" href="./__default.html" class="gray enabled heyo" cx="600" cy="300" r="8" />
        <circle name="Ending 3" href="./__default.html" class="gray enabled heyo" cx="700" cy="100" r="8" />
        <circle name="Crypto Caulilingo" href="./71_CryproCaulilingo/README.html" class="yellow enabled heyo" cx="700" cy="300" r="8" />
        <circle name="Gate Lock" href="./80_GateLock/README.html" class="darkgreen enabled heyo" cx="800" cy="200" r="8" />
        <circle name="Ending 4" href="./__default.html" class="gray enabled heyo" cx="900" cy="200" r="8" />
    <div class="description">bla</div>
    <script>
    var script = document.createElement('script');
    script.src = 'http://code.jquery.com/jquery-1.11.0.min.js';
        $description = $(".description");
        $('circle').hover(function() {
            $description.addClass('active');
            $description.html($(this).attr('name'));
        }, function() {
            $description.removeClass('active');
        });
        $(document).on("click", ".enabled", function(e){
            document.location = $(this).attr('href');
        });
        $(document).on('mousemove', function(e){
            $description.css({
            left:  e.pageX,
            top:   e.pageY - 70
            });
        });
    </script>
    </svg>

#### [Enter Space-Time Coordinates](./00_EnterSpaceTimeCoordinates/README.md)
#### [Ad](./01_Ad/README.md)
#### [Satellite](./10_Satellite/README.md)
#### [HomeComputer](./10_Satellite/README.md)
#### [Work Computer](./21_WorkComputer/README.md)
#### [Government Agriculture Network](./30_GovernmentAgricultureNetwork/README.md)
#### [STOP GAN](./40_STOP_GAN/README.md)
#### [CookieWorldOrder](./51_CookieWorldOrder/README.md) 
#### [FriendSpaceBookPlusAllAccessRedPremium](./52_FriendSpaceBookPlusAllAccessRedPremium/README.md)
#### [Drive to the target](./60_DriveToTheTarget/README.md)
#### [Crypto Caulingo](./71_CryptoCaulingo/README.md)
#### [Gate Lock](./80_GateLock/README.md)
