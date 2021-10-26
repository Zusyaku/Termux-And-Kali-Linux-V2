# code by polygon
#_________________require_____________#
require 'colorize'
require 'net/http'
require 'thread'
require 'lolcat'
require 'rand'
require 'requests'
require 'uri'
#____________________definisi nya______________#

def load()
puts ""
  co = 0
    while co <= 100
       sleep 0.1
       print "\r\e[97m\e[5mLoading \e[5m\e[96m"
       print co
       co = co.to_i + 1
    end
end

def self.get_random
    rand(255)
  end

  def self.color_hex(options = {})
    default = { red: get_random, green: get_random, blue: get_random }
    options = default.merge(options)
    '#%X%X%X' % options.values
  end

def self.load2
    system "clear"
    com = "📁>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    80.times do
      system "clear"
      puts com.bold.cyan
      new_circles = com.insert(0, "/")
      new_circles.slice!(new_circles.length-1,new_circles.length)
      circles = new_circles
      sleep(0.06)
    end
   
  end  
  
def penj()
     system "clear"
     system "sleep 2"
     puts "\e[93m<=====\e[91m==========\e[94m==========\e[91m=========\e[93m====>"
     system "sleep 0.09"
     puts "           \e[93mmasukan nilai \e[91mawal"
     system "sleep 0.09"
     puts ""
     system "sleep 0.09"
     print "\e[92m[× \e[97m~\e[91m>\e[92m ×]\e[96m "
     aw = gets.chomp()
     system "sleep 0.09"
     puts ""
     system "sleep 0.1"
     puts "\e[92mMasukan \e[91mnilai \e[92makhir"
     system "sleep 0.1"
     print "\e[97m=\e[93m=\e[92m>\e[95m "
     ak = gets.chomp()
     system "sleep 0.1"
     puts ""
     system "sleep 0.1"
     print "\e[92mHasil \e[91m: \e[93m"
     print (aw.to_i + ak.to_i)
     puts ""
     system "sleep 0.2"
     puts ""
 end

def kali()
    system "clear"
    puts "\e[92m<=======\e[91m========\e[94m=========\e[92m======>"
    puts "         \e[93mmode \e[91mperkalian\e[00m"
    puts "\e[92m=======\e[93m=========\e[94m=========\e[92m======>"
    puts ""
    puts "\e[96mmasukan nilai awal"
    print "\e[92m[\e[93m~\e[96m$\e[92m]\e[97m "
    pa = gets.chomp()
    puts ""
    puts "\e[94mmasukan nilai akhir "
    print "\e[92m[\e[93m~\e[92m$\e[92m]\e[97m "
    su = gets.chomp()
    puts ""
    system "sleep 1"
    print "   \e[97mhasil \e[91m: \e[97m"
    has = (pa.to_i * su.to_i)
    print "#{has}"
end
    
def bagi()
    system "clear"
    puts "\e[92m<=======\e[91m========\e[94m=========\e[92m======>"
    puts "         \e[93mmode \e[91mpembagian\e[00m"
    puts "\e[92m=======\e[93m=========\e[94m=========\e[92m======>"
    puts ""
    puts "masukan nilai awal".bold.cyan
    print "\e[92m[\e[93m~\e[91m$\e[92m]\e[97m "
    to = gets.chomp()
    puts ""
    puts "\e[94mmasukan nilai akhir"
    print "\e[92m[\e[93m~\e[92m$\e[92m]\e[97m "
    d = gets.chomp()
    puts ""
    system "sleep 1"
    print "   \e[97mhasil \e[91m: \e[97m"
    has = (to.to_i / d.to_i)
    i = 0

  while i <= has
     system "sleep 0.1"
     print "\rhasil \e[91m: \e[00m"
     print i
     i = i.to_i + 1
 end
 
end

def kur()
    system "clear"
    puts "\e[92m<=======\e[91m========\e[94m=========\e[92m======>"
    puts "         \e[93mmode \e[91mperkurangan\e[00m"
    puts "\e[92m=======\e[93m=========\e[94m=========\e[92m======>"
    puts ""
    puts "\e[96mmasukan nilai awal"
    print "\e[92m[\e[93m~\e[92m$\e[92m]\e[97m "
    pa = gets.chomp()
    puts ""
    puts "\e[94mmasukan nilai akhir"
    print "\e[92m[\e[93m~\e[93m$\e[92m]\e[97m "
    su = gets.chomp()
    puts ""
    system "sleep 1"
    print "   \e[97mhasil \e[91m: \e[97m"
    has = (pa.to_i - su.to_i)
    print "#{has}"
end

#________________banner_______________#
def banner()
sleep 1
puts "         \e[91m\e[5m█ █ █▀▀█ █   █ █ █──█ █   █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ "
sleep 0.08
puts "         \e[97m\e[5m█▀▄ █▄▄█ █   █▀▄ █──█ █   █▄▄█   █   █──█ █▄▄▀ "
sleep 0.08
puts "         ▀ ▀ ▀  ▀ ▀▀▀ ▀ ▀  ▀▀▀ ▀▀▀ ▀  ▀   ▀   ▀▀▀▀ ▀ ▀▀".bold.white
sleep 0.09
end
 
		    
#____________________________display___________________________#

     def self.disp
          puts "\e[92m<===========================\e[91m\\\\\\\\\e[93m[@menu]\e[91m\\\\\\\\\e[92m================================>"
      end
   def dis()
       sleep 0.1
       disp
       sleep 0.1
       puts "\e[96m1\e[95m)\e[97mpenjumlahan"
       sleep 0.1
       puts "\e[96m2\e[95m)\e[97mpengurangan"
       sleep 0.1
       puts "\e[96m3\e[95m)\e[97mperkalian"
       sleep 0.1
       puts "\e[96m4\e[95m)\e[97mpembagian"
       sleep 1
       sleep 0.1
       disp
       sleep 0.1
 end
           def self.int
                load2
                sleep 0.1
                puts ""
                sleep 0.1
                puts"
          \e[93mauthor       \e[94m: \e[97mpolygon
          \e[91mmy \e[97myoutube   \e[92m: \e[93mpejuang kentang
          "
                sleep 0.1
               
	        puts ""
               puts "\e[92m<=======\e[91m========\e[94m=============\e[91m======\e[94m===========\e[91m=========\e[94m=======\e[92m=====>"
       end

                 def self.menu
                   sleep 0.1
                   int
                   sleep 0.1
                   puts ""
		   sleep 0.1
                   banner
		   sleep 0.1
             end
def self.ip
       ip = system "curl ifconfig.me"
    end

def self.keyword
 menu
puts ""
sleep 1
print "\r\e[92mip \e[97mkamu\e[93m[\e[96m"
ip
print "\e[93m]"
sleep 1
puts ""
dis
sleep 1
puts ""
sleep 0.1
print "\e[92m\e[5m[\e[93m@Menu\e[92m]\e[93m>\e[95m "
me = gets.chomp()

if me == "1"
   load
  sleep 1
   penj
puts ""
puts "\e[92mgunakan \e[93mlagi \e[92my \e[93m/ \e[91mt"
     print "\e[91m>\e[93m>\e[95m"
     ke = gets.chomp
if ke == "y"
   load
   sleep 1
   penj
end
if ke == "t"
   load
   sleep 1
   system "xdg-open https://youtube.com/channel/UCtu-GcxKL8kJBXpR1wfMgWg"
   sleep 3
   system "toilet -f bigmono9 -F gay subrek"
   system "exit 1"
end
 end

if me == "2"
   load
  sleep 1
   kur
puts ""
puts "\e[92mgunakan \e[93mlagi \e[92my \e[93m/ \e[91mt"
     print "\e[91m>\e[93m>\e[95m"
     ke = gets.chomp
if ke == "y"
   load
   sleep 1
   kur
end
if ke == "t"
   load
   sleep 1
   system "xdg-open https://youtube.com/channel/UCtu-GcxKL8kJBXpR1wfMgWg"
   sleep 3
   system "toilet -f bigmono9 -F gay subrek"
   system "exit 1"
end
 end

if me == "3"
   load
  sleep 1
   kali
puts ""
puts "\e[92mgunakan \e[93mlagi \e[92my \e[93m/ \e[91mt"
     print "\e[91m>\e[93m>\e[95m"
     ke = gets.chomp
if ke == "y"
   load
   sleep 1
   kali
end
if ke == "t"
   load
   sleep 1
   system "xdg-open https://youtube.com/channel/UCtu-GcxKL8kJBXpR1wfMgWg"
   sleep 3
   system "toilet -f bigmono9 -F gay subrek"
   system "exit 1"
end
 end

if me == "4"
   load
  sleep 1
   bagi
puts ""
puts "\e[92mgunakan \e[93mlagi \e[92my \e[93m/ \e[91mt"
     print "\e[91m>\e[93m>\e[95m"
     ke = gets.chomp
if ke == "y"
   load
   sleep 1
   bagi
end
if ke == "t"
   load
   sleep 1
   system "xdg-open https://youtube.com/channel/UCtu-GcxKL8kJBXpR1wfMgWg"
   sleep 3
   system "toilet -f bigmono9 -F gay subrek"
   system "exit 1"
end
else
    sleep 1
    puts "\e[93mKeyword \e[91meror \e[97m#{me}"
   sleep 3
keyword
 end
end
keyword
