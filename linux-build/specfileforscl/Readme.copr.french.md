Comment créer les paquets rpm en Utilisant Fedora Copr pour Linux
=====
<p><h3><a href="Readme.french.md" target="_blank">Accueil Comment créer les paquets pour Linux</a></h3></p>
<div>
  <span>Français</span> / <a href="Readme.copr.md">English</a>
</div></br>
<p>Ce Tutoriel vous explique comment créer des paquets rpm en Utilissant Fedora Copr</p>
<p>Si vous le souhaitez vous pouvez utiliser <a href="Readme.french.md" target="_blank">un autre système de compilation</a></p>
<p>Pour commencer vous devez disposer d'un Compte Fedora</p>
<p>Si vous n'avez pas de Compte Fedora</p>
<p>Rendez-vous sur <a href="https://accounts.fedoraproject.org/" target="_blank">accounts.fedoraproject.org</a></p>
<p>pour créer votre compte gratuitement</p>
<p>Une fois votre compte créer Rendez-vous sur <a href="https://copr.fedorainfracloud.org/" target="_blank">Fedora Copr</a></p>
</br></br>
<a href="https://imgur.com/lMIyzXp.png" target="_blank">
  <img src="https://imgur.com/lMIyzXp.png" />
</a></br></br>
<p><h3>Cliquez sur login en haut à droite</h3></p></br></br>
<a href="https://imgur.com/udp4Yop.png" target="_blank">
  <img src="https://imgur.com/udp4Yop.png" />
</a></br></br>
<p><h3>Connectez vous avec votre Compte Fedora</h3></p></br></br>
<p><h3>si vous avez une erreur recharger la page</h3></p></br></br>
<p><a href="https://copr.fedorainfracloud.org/login/" target="_blank">https://copr.fedorainfracloud.org/login/</a></p></br></br>
<a href="https://imgur.com/BkN1vGN.png" target="_blank">
  <img src="https://imgur.com/BkN1vGN.png" />
</a></br></br>
<p><h3>Si une fenètre d'autorisation s'affiche autoriser la connexion</p></h3></br></br>
<a href="https://imgur.com/ameTp2f.png" target="_blank">
  <img src="https://imgur.com/ameTp2f.png" />
</a></br></br>
<p><h3>Cliquez sur New Project</p></h3></br></br>
<a href="https://imgur.com/VgrV309.png">
  <img src="https://imgur.com/VgrV309.png" />
</a></br></br>
<p><h3>Remplissez les informations du projet comme ceci</p></h3></br></br>
<a href="https://imgur.com/5Sc5tRo.png">
  <img src="https://imgur.com/5Sc5tRo.png" />
</a></br></br>
<a href="https://imgur.com/nKsPZkX.png">
  <img src="https://imgur.com/nKsPZkX.png" />
</a></br></br>
<a href="https://imgur.com/6Kg3Sph.png">
  <img src="https://imgur.com/6Kg3Sph.png" />
</a></br></br>
<a href="https://imgur.com/jRtBlft.png">
  <img src="https://imgur.com/jRtBlft.png" />
</a></br></br>
<a href="https://imgur.com/VtTCJnR.png">
  <img src="https://imgur.com/VtTCJnR.png" />
</a></br></br>
<a href="https://imgur.com/kURWXEQ.png">
  <img src="https://imgur.com/kURWXEQ.png" />
</a></br></br>
<p><h3>Tient des repos externe mais c'est quoi ces repos</p></h3></br></br>
<a href="https://rpmfusion.org/">Explication en l'Anglais (Langue d'Origine)</a></br></br>
<a href="https://rpmfusion-org.translate.goog/?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=fr&_x_tr_pto=wapp">Explication traduite en français</a></br></br>
<p><h3>Pour comparer avec d'autre distribution Linux l'activation de rpmfusion correspond</p></h3></br></br>
<p><h3>Pour Debian a l'activation des dépots contrib nonfree et debian multimedia</p></h3></br></br>
<p><h3>Pour Ubuntu a l'activation des dépots universe et multiverse</p></h3></br></br>
<a href="https://imgur.com/Di0WE9N.png">
  <img src="https://imgur.com/Di0WE9N.png" />
</a></br></br>
<a href="https://imgur.com/9cwyMvm.png">
  <img src="https://imgur.com/9cwyMvm.png" />
</a></br></br>
<a href="https://imgur.com/AHgpJCC.png">
  <img src="https://imgur.com/AHgpJCC.png" />
</a></br></br>
<p><h3>Cliquez sur Create</p></h3></br></br>
<a href="https://imgur.com/AMIfIZn.png">
  <img src="https://imgur.com/AMIfIZn.png" />
</a></br></br>
<p><h3>Félicitation vous venez de créez un nouveau projet sur Fedora Copr</p></h3></br></br>
<p><h3>Maintenant que notre projet est créer nous allons créer notre premier pacquet rpm</p></h3></br></br>
<p><h3>Etant donné que nous allons créer nos paquets en Software Collection</p></h3></br></br>
<p><h3>C'est quoi un Software Collection pour plus d'information a ce sujet je vous renvoie vers les pages web suivante</p></h3></br></br>
<a href="https://www.softwarecollections.org/en/">Site Officiel du projet Software Collection (Anglais Langue d'origine)</a></br></br>
<a href="https://www-softwarecollections-org.translate.goog/en/?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=fr&_x_tr_pto=wapp">Site Officiel du projet Software Collection traduit en Français</a></br></br>
<a href="https://access.redhat.com/documentation/en-us/red_hat_software_collections/2/html/packaging_guide/index">Documentation Officiel RHEL (Red Hat Entreprise Linux) sur la création des Software Collection (Necéssite un compte RHEL)</a></br></br>
<p><h3>Cliquez sur Packages</p></h3></br></br>
<a href="https://imgur.com/AoSLCqq.png">
  <img src="https://imgur.com/AoSLCqq.png" />
</a></br></br>
<p><h3>Cliquez sur New Package</p></h3></br></br>
<a href="https://imgur.com/xNFANv8.png">
  <img src="https://imgur.com/xNFANv8.png" />
</a></br></br>
<p><h3>Cliquez sur Custom</p></h3></br></br>
<a href="https://imgur.com/SZKBEDy.png">
  <img src="https://imgur.com/SZKBEDy.png" />
</a></br></br>
<p><h3>Remplissez les informations comme indiqué sur la photo</h3></p></br></br>
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
<p><h3>Cliquez sur Save</p></h3></br></br>
<a href="https://imgur.com/BMwq1Wr.png">
  <img src="https://imgur.com/BMwq1Wr.png" />
</a></br></br>
<p><h3>Dans la cologne scl-utils Cliquez sur le bouton Rebuild en dessous de Actions</h3></p>
<a href="https://imgur.com/P9qc8YS.png">
  <img src="https://imgur.com/P9qc8YS.png" />
</a></br></br>
<a href="https://imgur.com/ahSMpPm.png">
  <img src="https://imgur.com/ahSMpPm.png" />
</a></br></br>
<p><h3>Cliquez sur Build pour commencer la création du rpm sur Fedora Copr</h3></p>
<a href="https://imgur.com/n7OULET.png">
  <img src="https://imgur.com/n7OULET.png" />
</a></br></br>
<p><h3>Attendez un moment puis réactualiser la page jusqu'à ce que la compilation soit terminer</h3></p>
<a href="https://imgur.com/WM4nh7w.png">
  <img src="https://imgur.com/WM4nh7w.png" />
</a></br></br>
