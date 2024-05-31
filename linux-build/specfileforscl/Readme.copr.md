How to create rpm packages using Fedora Copr for Linux
=====
<div>
  <span>English</span> / <a href="Readme.copr.french.md">Français</a>
</div></br>
<p>This Tutorial explains how to create rpm packages using Fedora Copr</p>
<p>If you wish you can use <a href="Readme.md" target="_blank">another compilation system</a></p>
<p>To get started you must have a Fedora Account</p>
<p>If you don't have a Fedora Account</p>
<p>Visit <a href="https://accounts.fedoraproject.org/">accounts.fedoraproject.org</a></p>
<p>to create your account for free</p>
<p>Once your account is created, Visit <a href="https://copr.fedorainfracloud.org/">Fedora Copr</a></p>
</br></br>
<a href="https://i.imgur.com/lMIyzXp.png">
  <img src="https://i.imgur.com/lMIyzXp.png" />
</a></br></br>
<p>Click on login at the top right</p></br></br>
<a href="https://i.imgur.com/udp4Yop.png">
  <img src="https://i.imgur.com/udp4Yop.png" />
</a></br></br>
<p><h3>Log in with your Fedora Account</h3></p></br></br>
<p><h3>If you have an error reload the page</h3></p></br></br>
<p><a href="https://copr.fedorainfracloud.org/login/">https://copr.fedorainfracloud.org/login/</a></p></br></br>
<a href="https://i.imgur.com/BkN1vGN.png">
  <img src="https://i.imgur.com/BkN1vGN.png" />
</a></br></br>
<p><h3>If an authorization window appears, authorize the connection</p></h3></br></br>
<a href="https://i.imgur.com/ameTp2f.png" target="_blank">
  <img src="https://i.imgur.com/ameTp2f.png" />
</a></br></br>
<p><h3>Click New Project</p></h3></br></br>
<a href="https://i.imgur.com/JU8KoZB.png">
  <img src="https://i.imgur.com/JU8KoZB.png" />
</a></br></br>
<p><h3>Fill in the project information like this</p></h3></br></br>
<a href="https://i.imgur.com/5Sc5tRo.png">
  <img src="https://i.imgur.com/5Sc5tRo.png" />
</a></br></br>
<a href="https://i.imgur.com/nKsPZkX.png">
  <img src="https://i.imgur.com/nKsPZkX.png" />
</a></br></br>
<a href="https://i.imgur.com/6Kg3Sph.png">
  <img src="https://i.imgur.com/6Kg3Sph.png" />
</a></br></br>
<a href="https://i.imgur.com/jRtBlft.png">
  <img src="https://i.imgur.com/jRtBlft.png" />
</a></br></br>
<a href="https://i.imgur.com/VtTCJnR.png">
  <img src="https://i.imgur.com/VtTCJnR.png" />
</a></br></br>
<a href="https://i.imgur.com/kURWXEQ.png">
  <img src="https://i.imgur.com/kURWXEQ.png" />
</a></br></br>
<p><h3>Holds external repositories but what are these reports</p></h3></br></br>
<a href="https://rpmfusion.org/">Explanation</a></br></br>
<p><h3>To compare with other Linux distributions, activation of rpmfusion corresponds</p></h3></br></br>
<p><h3>For Debian, the contrib nonfree and debian multimedia repositories are activated</p></h3></br></br>
<p><h3>For Ubuntu, the universe and multiverse repositories are activated</p></h3></br></br>
<a href="https://i.imgur.com/Di0WE9N.png">
  <img src="https://i.imgur.com/Di0WE9N.png" />
</a></br></br>
<a href="https://i.imgur.com/9cwyMvm.png">
  <img src="https://i.imgur.com/9cwyMvm.png" />
</a></br></br>
<a href="https://i.imgur.com/AHgpJCC.png">
  <img src="https://i.imgur.com/AHgpJCC.png" />
</a></br></br>
<p><h3>Click Create</p></h3></br></br>
<a href="https://i.imgur.com/gCWq5G0.png">
  <img src="https://i.imgur.com/gCWq5G0.png" />
</a></br></br>
<p><h3>Congratulations, you have just created a new project on Fedora Copr</p></h3></br></br>
<p><h3>Now that our project is created we will create our first rpm package</p></h3></br></br>
<p><h3>Since we are going to create our packages in Software Collection</p></h3></br></br>
<p><h3>What is a Software Collection for more information on this subject I refer you to the following web pages</p></h3></br></br>
<a href="https://www.softwarecollections.org/en/">Official Website of the Software Collection project</a></br></br>
<a href="https://access.redhat.com/documentation/en-us/red_hat_software_collections/2/html/packaging_guide/index">Official RHEL (Red Hat Enterprise Linux) documentation on creating Software Collections (Requires a RHEL account)</a></br></br>
<p><h3>Click Packages</p></h3></br></br>
<a href="https://i.imgur.com/AoSLCqq.png">
  <img src="https://i.imgur.com/AoSLCqq.png" />
</a></br></br>
<p><h3>Click New Package</p></h3></br></br>
<a href="https://i.imgur.com/xNFANv8.png">
  <img src="https://i.imgur.com/xNFANv8.png" />
</a></br></br>
<p><h3>Click Custom</p></h3></br></br>
<a href="https://imgur.com/SZKBEDy.png">
  <img src="https://imgur.com/SZKBEDy.png" />
</a></br></br>
<p><h3>Fill in the information as shown in the photo</p></h3></br></br>
<a href="../../../raw/develop/linux-build/specfileforscl/scl-utils.spec">scl-utils.spec</a></br></br>
<code>#!/bin/sh -x
wget https://github.com/andykimpe/PokemonStudio/raw/develop/linux-build/specfileforscl/scl-utils/copr-custom.sh -O copr-custom.sh
bash copr-custom.sh
rm -f copr-custom.sh</code></br></br>
<a href="https://imgur.com/CVAKsfD.png">
  <img src="https://imgur.com/CVAKsfD.png" />
</a></br></br>
<code>#!/bin/sh -x
wget [https://github.com/andykimpe/PokemonStudio](https://github.com/PokemonWorkshop/PokemonStudio)/raw/develop/linux-build/specfileforscl/scl-utils/copr-custom.sh -O copr-custom.sh
bash copr-custom.sh
rm -f copr-custom.sh</code></br></br>
<a href="https://imgur.com/UjpiJeD.png">
  <img src="https://imgur.com/UjpiJeD.png" />
</a></br></br>
<p><h3>Click Save</p></h3></br></br>
<a href="https://imgur.com/BMwq1Wr.png">
  <img src="https://imgur.com/BMwq1Wr.png" />
</a></br></br>
<p><h3>In cologne scl-utils Click the Rebuild button below Actions</h3></p>
<a href="https://imgur.com/P9qc8YS.png">
  <img src="https://imgur.com/P9qc8YS.png" />
</a></br></br>
<a href="https://imgur.com/ahSMpPm.png">
  <img src="https://imgur.com/ahSMpPm.png" />
</a></br></br>
<p><h3>Click Build to start creating the rpm on Fedora Copr</h3></p>
<a href="https://imgur.com/n7OULET.png">
  <img src="https://imgur.com/n7OULET.png" />
</a></br></br>
<p><h3>Wait a moment then refresh the page until the compilation is complete</h3></p>
<a href="https://imgur.com/WM4nh7w.png">
  <img src="https://imgur.com/WM4nh7w.png" />
</a></br></br>
