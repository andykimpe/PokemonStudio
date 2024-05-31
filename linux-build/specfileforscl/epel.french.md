<h1>Extra Packages for Enterprise Linux (EPEL)</h1>
<p><h3><a href="Readme.french.md" target="_blank">Accueil Comment créer les paquets pour Linux</a></h3></p>
<p><h3>Packages supplémentaires pour Enterprise Linux (EPEL)</h3></p>
<a href="https://docs.fedoraproject.org/en-US/epel/_images/epel-logo.svg" target="_blank">
  <img src="https://docs.fedoraproject.org/en-US/epel/_images/epel-logo.svg" />
</a></br></br>
<p>Bienvenue dans la maison du Groupe d’Intérêt Spécial EPEL.</p>
<p>L'objectif d'EPEL est de rendre disponibles des packages Fedora de haute qualité pour RHEL et ses dérivés compatibles.</p>
<p><h3>Démarrage rapide</h3></p>
<p>Nous proposons des packages de version contenant nos fichiers de configuration de référentiel et des clés de signature de packages publics. Utilisez la version qui correspond à la version majeure de votre système d'exploitation.</p>
<p><a href="https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm" target="_blank">epel-release-latest-9</a></p>
<p><a href="https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm" target="_blank">epel-release-latest-8</a></p>
<p><a href="https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm" target="_blank">epel-release-latest-7</a></p>
<p>Si vous utilisez CentOS (Community enterprise Operating System) Stream, nous vous recommandons également d'installer le package epel-next-release correspondant.</p>
<p><a href="https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-9.noarch.rpm" target="_blank">epel-next-release-latest-9</a></p>
<p><a href="https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-8.noarch.rpm" target="_blank">epel-next-release-latest-8</a></p>
<p>Pour plus de commodité, certaines distributions incluent ces packages de versions dans leurs référentiels par défaut, vous permettant de les installer par leur nom sans l'URL complète.</p>
<p>Certains packages EPEL dépendent de packages provenant de référentiels qui ne sont pas activés par défaut. Prenez note des référentiels supplémentaires activés dans les instructions suivantes.</p>
<p><h3>EL9 (Entreprise Linux 9)</h3></p>
<p><h3>CentOS (Community enterprise Operating System) Stream 9</h3></p>
<p><code>sudo dnf -y config-manager --set-enabled crb
sudo dnf -y install epel-release epel-next-release</code></p>
<p><h3>RHEL (Red Hat Entreprise Linux) 9</h3></p>
<p><code>sudo subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
sudo dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm</code></p>
<p><h3>AlmaLinux 9, Rocky Linux 9 et autres fork</h3></p>
<p><code>sudo dnf config-manager --set-enabled crb
sudo dnf -y install epel-release</code></p>
<p><h3>EL8 (Entreprise Linux 8)</h3></p>
<p><h3>CentOS (Community enterprise Operating System) Stream 8</h3></p>
<p><code>sudo dnf config-manager --set-enabled powertools
sudo dnf -y install epel-release epel-next-release</code></p>
<p><h3>RHEL (Red Hat Entreprise Linux) 8</h3></p>
<p><code>sudo subscription-manager repos --enable codeready-builder-for-rhel-8-$(arch)-rpms
sudo dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm</code></p>
<p><h3>AlmaLinux 8, Rocky Linux 8 et autres fork</h3></p>
<p><code>sudo dnf config-manager --set-enabled powertools
sudo dnf -y install epel-release</code></p>
<p><h3>EL7 (Entreprise Linux 7)</h3></p>
<p><h3>RHEL (Red Hat Entreprise Linux) 7</h3></p>
<p><code>sudo subscription-manager repos --enable rhel-*-optional-rpms \
                           --enable rhel-*-extras-rpms \
                           --enable rhel-ha-for-rhel-*-server-rpms
sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm</code></p>
<p><h3>CentOS (Community enterprise Operating System) 7</h3></p>
<p><code>sudo yum -y install epel-release</code></p>
<p><h3>EL6 (Entreprise Linux 6)</h3></p>
<p><h3>RHEL (Red Hat Entreprise Linux) 6</h3></p>
<p><code>sudo subscription-manager repos --enable rhel-*-optional-rpms \
                           --enable rhel-*-extras-rpms \
                           --enable rhel-ha-for-rhel-*-server-rpms
sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm</code></p>
<p><h3>CentOS (Community enterprise Operating System) 6</h3></p>
<p><code>sudo yum -y install epel-release</code></p>
<p><h1>Qu'est-ce que les packages supplémentaires pour Enterprise Linux (ou EPEL) ?</h1></p>
<p>Extra Packages for Enterprise Linux (ou EPEL) est un groupe d'intérêt spécial de Fedora qui crée, maintient et gère un ensemble de packages supplémentaires de haute qualité pour Enterprise Linux, notamment, mais sans s'y limiter, Red Hat Enterprise Linux (RHEL), CentOS (Community enterprise Operating System), Scientific Linux (SL), Oracle Linux (OL), AlmaLinux (AL) et Rocky Linux (RL).</p>
<p>Les packages EPEL sont généralement basés sur leurs homologues Fedora et ne doivent pas entrer en conflit ou remplacer les packages des distributions de base Enterprise Linux. EPEL utilise en grande partie la même infrastructure que Fedora, notamment le système de construction, l'instance Bugzilla, le gestionnaire de mises à jour, le gestionnaire de miroirs, etc.</p>
<p>Apprenez-en davantage sur l’EPEL dans les pages suivantes :</p>
<p><a href="https://docs.fedoraproject.org/en-US/epel/epel-faq" target="_blank">EPEL FAQ (Non traduit Uniquement en Anglais)</a></p>
<p><a href="https://docs.fedoraproject.org/en-US/epel/epel-about" target="_blank">À propos d'EPEL (Non traduit Uniquement en Anglais)</a></p>
<p><a href="https://docs.fedoraproject.org/en-US/epel/epel-policy" target="_blank">EPEL FAQ (Non traduit Uniquement en Anglais)</a></p>
<p><h1>Qu’est-ce qu’EPEL-Next ?</h1></p>
<p>Les packages EPEL sont construits avec RHEL (Red Hat Entreprise Linux). Les packages EPEL Next sont construits sur CentOS (Community enterprise Operating System) Stream.</p>
<p>EPEL-Next n'est pas une reconstruction complète de tous les packages EPEL, mais uniquement des packages qui doivent être reconstruits pour être installés sur CentOS Stream. Le référentiel EPEL-Next est destiné à être superposé au référentiel EPEL standard.</p>
<p>Apprenez-en davantage sur EPEL-Next sur la page suivante :</p>
<p><a href="https://docs.fedoraproject.org/en-US/epel/epel-about-next" target="_blank">EPEL Next (Non traduit Uniquement en Anglais)</a></p>
<p><h1>Quels packages et versions sont disponibles dans EPEL ?</h1></p>
<p>Étant donné qu'EPEL fait partie du projet Fedora, vous pouvez rechercher les packages disponibles dans <a href="https://packages.fedoraproject.org/" target="_blank">l' application Web Fedora Packages (Non traduit Uniquement en Anglais)</a> . Cela donne un aperçu des versions disponibles dans les différentes branches EPEL. Si vous trouvez un package qui n'est pas encore disponible dans l'agence EPEL et que vous souhaiteriez qu'il le soit, veuillez suivre ce <a href="https://docs.fedoraproject.org/en-US/epel/epel-package-request/" target="_blank">guide (Non traduit Uniquement en Anglais)</a> pour le demander.</p>
<p>Alternativement, vous pouvez parcourir directement les fichiers du dépôt :</p>
<p>EPEL 9 : <a href="https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/" target="_blank">x86_64</a> , <a href="https://dl.fedoraproject.org/pub/epel/9/Everything/s390x/" target="_blank"> s390x</a> , <a href="https://dl.fedoraproject.org/pub/epel/9/Everything/ppc64le/" target="_blank"> ppc64le</a> , <a href="https://dl.fedoraproject.org/pub/epel/9/Everything/aarch64/" target="_blank"> aarch64</a> , <a href="https://dl.fedoraproject.org/pub/epel/9/Everything/source/tree/" target="_blank"> sources</a></p>
<p>EPEL 8 : <a href="https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/" target="_blank">x86_64</a> , <a href="https://dl.fedoraproject.org/pub/epel/8/Everything/s390x/" target="_blank"> s390x</a> , <a href="https://dl.fedoraproject.org/pub/epel/8/Everything/ppc64le/" target="_blank"> ppc64le</a> , <a href="https://dl.fedoraproject.org/pub/epel/8/Everything/aarch64/" target="_blank"> aarch64</a> , <a href="https://dl.fedoraproject.org/pub/epel/8/Everything/SRPMS/" target="_blank"> sources</a></p>
<p>EPEL 7 : <a href="https://dl.fedoraproject.org/pub/epel/7/Everything/x86_64/" target="_blank">x86_64</a> , <a href="https://dl.fedoraproject.org/pub/epel/7/Everything/s390x/" target="_blank"> s390x</a> , <a href="https://dl.fedoraproject.org/pub/epel/7/Everything/ppc64le/" target="_blank"> ppc64le</a> , <a href="https://dl.fedoraproject.org/pub/epel/7/Everything/SRPMS/" target="_blank"> sources</a>(EPEL-7 pour aarch64 n'est plus pris en charge car Red Hat a mis fin à la prise en charge de cette architecture).</p>
<p>Vous pouvez également parcourir ces mêmes répertoires sur n'importe lequel de nos <a href="https://admin.fedoraproject.org/mirrormanager/mirrors/EPEL" target="_blank">miroirs</a> .</p>
<p>Pour plus de détail voir laa page d'origine en anglais.</p>
<p><h3><a href="https://docs.fedoraproject.org/en-US/epel/" target="_blank">Extra Packages for Enterprise Linux (EPEL)</a></h3></p>
<p><h3><a href="Readme.french.md" target="_blank">Accueil Comment créer les paquets pour Linux</a></h3></p>
