#!/data/data/com.termux/files/usr/bin/bash

#//////////////////////////////////////////////
#            --[ code by polygon ]--          #
#                                             #
#                                             #
# author : polygon                            #
# github : https://github.com/Bayu12345677    #
# note   : serah lu mau recode apa gak karma  #
#           masi berlaku :)                   #
###############################################


readonly awk=gawk

req=/data/data/com.termux/files/usr/bin/curl

if (source make.sh 2>/dev/null 1>/dev/null); then
          sleep 0.1
   else
        (
         : ${make:=null}
         {
          : ${make:=.}
          (
           printf "\e[92m[\e[91mx\e[92m]\e[00m make.sh tidak di temukan\n"

             /data/data/com.termux/files/usr/bin/sleep 0.1
                  exit 222
         );
      };
   ); exit 2
       fi

source make.sh
net=`
     $req --location \
           --request GET \
                  --silent \
                  --connect-timeout 7 \
                   --max-time 7 \
                    --url "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.xml"`

#### parse

tan=$(echo "$net" | awk -F"[<>]" '{ print $9 }' RS="</Tanggal>\n")
jam=$(echo "$net" | awk -F"[<>]" '{ print $13 }' RS="</jam>\n")
data=$(echo "$net" | awk -F"[<>]" '{ print $17 }' RS="</DateTime>\n")
cor=$(echo "$net" | awk -F"[<>]" '{ print $23 }' RS="</coordinates>\n")
lin=$(echo "$net" | awk -F"[<>]" '{ print $29 }' RS="</Lintang>\n")
bu=$(echo "$net" | awk -F"[<>]" '{ print $33 }' RS="</Bujur>\n")
mag=$(echo "$net" | awk -F"[<>]" '{ print $37 }' RS="</Magnitude>\n")
ked=$(echo "$net" | awk -F"[<>]" '{ print $41 }' RS="</Kedalaman>\n")
wil=$(echo "$net" | awk -F"[<>]" '{ print $45 }' RS="</Wilayah>\n")
pot=$(echo "$net" | awk -F"[<>]" '{ print $49 }' RS="</Potensi>\n")

: ${tan:=tanggal}
: ${jam:=jam}
: ${data:=data-req}
: ${cor:=coordinat}
: ${lin:=lintang}
: ${bu:=bujur}
: ${mag:=magnitude}
: ${ked:=kedalaman}
: ${wil:=wilayah}
: ${pot:=potensi}


##########################################################################

            function __net__() {
                     request=`$1 --location \
                           --request GET \
                            --silent \
                             --connect-timeout 6 \
                            --max-time 6 \
                           --url "https://www.bmkg.go.id" | ${use[1]} |
                                                            tail +181 |
                                                            head -200`
             : ${__net__:=lynx -dump}
             : ${__net__:=w3m -dump}

                }


           function __init__()
{

                   local req; local host="https://www.bmkg.go.id"; local Request=GET
             (
               readonly main="curl"
             );

               dis=6

         line=( "545" );

             cut=( "40" );

            self_net=`$1 --location \
                          --request $Request \
                           --silent \
                         --connect-timeout ${dis} \
                             --max-time ${dis} \
                               --url "$host" | ${use[1]} |
                                              tail +${line[@]} |
                                               head -${cut[0]}`
}


                         function author {
                             local cc; cc=0; set cc;

                                  opt='while'

                                          local Text="author : polygon"
                                             local Text2="script bmkg by polygon"
                                               readonly one=${#Text}
                                                t=${#Text2}


                                     while ((cc<=100)); do
                                             n=$((cc*one / 80));
                                               printf "\\r                              \e[92m[\e[96m%-${one}s\e[92m]\e[00m" "${Text:0:n}"
                                                   ((cc += RANDOM%10))
                                                       time=$(sleep 0.1)
                                               done

                     local z=0
                                      while ((z<=100)); do
                                             n=$((z*t / 80));
                                               printf "\\r                           \e[91m[\e[93m%-${t}s\e[91m]\e[00m" "${Text2:0:n}"
                                                   ((z += RANDOM%10))
                                                       time=$(sleep 0.1)
                                               done

                                         : ${while:=Text}
                                   }


###########################################################################
for=( "setterm" )
parse=/data/data/com.termux/files/usr/bin/lynx

color=( "black" "red" "green" "yellow" "blue" "magenta" "cyan" "white" )

bla=$(${for[0]} --foreground ${color[0]} --bold on)   cy=$(${for[0]} --foreground ${color[6]} --bold on)
me=$(${for[0]} --foreground ${color[1]} --bold on)    bla=$(${for[0]} --foreground ${color[7]} --bold on)
ij=$(${for[0]} --foreground ${color[2]} --bold on)    st=$( printf '\e[00m' )
ku=$(${for[0]} --foreground ${color[3]} --bold on)
bi=$(${for[0]} --foreground ${color[4]} --bold on)
m=$(${for[0]} --foreground ${color[5]} --bold on)

function banner()
{
             echo -e "                      ${ij}██████${me}╗${ij} ███${me}╗${ij}   ███${me}╗${ij}██${me}╗  ${ij}██${me}╗ ${ij}██████${me}╗${st}"; sleep 0.1
             echo -e "                      ${ij}██${me}╔══${ij}██${me}╗${ij}████${me}╗ ${ij}████${me}║${ku}██${me}║ ${ku}██${me}╔╝${ku}██${me}╔════╝${st}"; sleep 0.1
             echo -e "                      ${cy}██████${me}╔╝${cy}██${me}╔${cy}████${me}╔${ij}██${me}║${ij}█████${me}╔╝ ${ij}██${me}║  ${ij}███${me}╗${st}"; sleep 0.1
             echo -e "                      ${cy}██${me}╔══${cy}██${me}╗${cy}██${me}║╚${cy}██${me}╔╝${cy}██${me}║${cy}██${me}╔═${cy}██${me}╗ ${cy}██${me}║   ${cy}██${me}║${st}"; sleep 0.1
             echo -e "                      ${bi}██████${me}╔╝${bi}██${me}║ ╚═╝ ${bi}██${me}║${ku}██${me}║  ${ku}██${me}╗╚${ku}██████${me}╔╝${st}"; sleep 0.1
             echo -e "                      ${me}╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝${st}"; sleep 0.1
};


      function __main__()
{
       /data/data/com.termux/files/usr/bin/clear
            (
              banner
              author; echo
          );

       toilet -f term -F gay "              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" | ${use[2]} -qL 270
                     echo -e "                         ${bi}[${ku}▶${bi}]${st} 1.data gempa terkini" | ${use[2]} -qL 90
                     echo -e "                         ${ku}[${cy}▶${ku}]${st} 2.prediksi cuaca" | ${use[2]} -qL 90
                     echo -e "                         ${ij}[${me}▶${ij}]${st} 3.prediksi udara" | ${use[2]} -qL 90
                     echo -e "                         ${cy}[${ku}▶${cy}]${st} 4.exit" | ${use[2]} -qL 90
       toilet -f term -F gay "              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" | ${use[2]} -qL 270
             local user=`whoami`
         echo -ne "              \e[92m[\e[91m@\e[96m${user}\e[92m]\e[94m~\e[95m> \e[93m" | ${use[2]} -qL 80; read select


      case $select in
                     1)shift; /data/data/com.termux/files/usr/bin/sleep 0.1
                         echo
                              function load()
                             {
                              local g; local frame="-_-_"

                                   until false :; do
                                        for((g=0; g<${#frame}; g++)); do
                                            time=$(sleep 0.1)
                                        printf "\r${m}[${ij}▶${m}]${me} Mem${ku}proses ${bi}[${cy}${frame:$g:1}${bi}]${st}"
                                          done; done
                             };

                                 (
                                   load &
                                      sleep 8
                                  kill "$!"
                                );

                                echo
                            echo; clear
                                 echo -e "       ${ij}====================${ku}================${bi}<${me}>${st}" | ${use[2]} -qL 270
                                 echo -e "       ${bi}|${ku}[${m}▶${ku}]${st} jam dan tanggal : ${cy}$jam${ij} – ${ku}$tan${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${m}[${cy}▶${m}]${st} data gempa${me}: ${ij}$data${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${me}[${ku}▶${me}]${st} koordinat ${me}: ${cy}$cor${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${ij}[${m}▶${me}]${st} lintang   ${me}: ${ku}$lin${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${ku}[${me}▶${ku}]${st} bujur     ${me}: ${ij}$bu${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${me}[${ij}▶${me}]${st} mangnitude: ${pu}$mag${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${ij}[${me}▶${ij}]${st} kedalaman ${me}: ${cy}$ked${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${ku}[${cy}▶${ku}]${st} Wilayah   ${me}: ${ij}$wil${st}"| ${use[2]} -qL 270
                                 echo -e "       ${bi}|${ij}[${bi}▶${ij}]${st} Potensi   ${me}: ${ku}$pot${st}" | ${use[2]} -qL 270
                          echo
                                 read -p $'\e[92m[\e[91m?\e[92m]\e[00m press enter ~ '; (__main__) ;;

                                2)shift; /data/data/com.termux/files/usr/bin/sleep 0.1


                                       {
                                            (

                                                   __net__ "curl"
                                               (
                                                  {
                                                    set gg; for((gg=0; gg<=100; gg++)); do
                                                                   time=$(sleep 0.02)
                                                               echo $gg
                                                                        done
                                                  } | ${use[3]} \
                                                                  --gauge "mencari data..." 6 70
                                                 ${use[3]} \
                                                             --title "prediksi cuaca" \
                                                             --msgbox "$request" 300 500; (__main__)
                                               );

                                            );
                                       };  ;;
                               3)shift; /data/data/com.termux/files/usr/bin/sleep 0.1
 : ${use:=3}
 : ${pwd:=-0}
                                   {
                                      (
                                         __init__ "curl"
                                      (
                                        {
                                         set mq
                                                 mq=0
                                          until false :; do
                                              sleep 0.03
                                            echo $mq
                                                     ((mq++))
                                            if [ $mq -eq 101 ]; then
                                                   break
                                             fi; done
                                         } | ${use[3]} \
                                                         --gauge "mencari data" 6 70

                                                    ${use[3]} \
                                                               --title "Kesehatan udara" \
                                                               --msgbox "$self_net" 300 500; (__main__)
                                       );
                                  );
                             }; ;;
                        4)sleep 0.1
                            echo "${ku}bye${st}"; sleep 7 && logout ;;
                        *)localtion=`pwd`
                          {
                           (
                            {
                               media=( "6" "70" )
                                syntax="404"
                                  msg="keyword Not found"

                                      intent=( "--title" "--msgbox" )

                                         set dialog

                                            if (ifconfig on 2>/dev/null 1>/dev/null); then
                                                     time=$(sleep 0.1)
                                              fi

                                       ${use[3]} \
                                                   ${intent[0]} "$syntax" \
                                                   ${intent[1]} "$msg" ${media[0]} \
                                                                       ${media[1]}; (__main__)
                               };
                           );
                       }; ;;
esac
}

       {
         (
           {
             : ${__main__:=yes}
               (__main__)
           };
        );
     };


