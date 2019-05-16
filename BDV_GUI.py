#Basketball DataVis (Data Visualization)
#pylint:disable = W0614
#By Robert Smith

#Import 
import tkinter
import os
from tkinter import *

#Create the main window
window = tkinter.Tk()
window.title("Basketball DataVis")
window.geometry("480x250")
window.configure(background = "grey")

#Data

GSW = {
       "Klay Thompson" : ((1461/73)),
       "Kevin Durant" : ((1792/68)),
       "Draymond Green" : ((773/70)),
       "Stephen Curry" : ((1346/51)),
       "Andre Iguodala" : ((384/64)),
       "Nick Young" : ((581/80)),
       "Shaun Livingstion" : ((394/71)),
       "David West" : ((495/73)),
       "Zaza Pachulia" : ((373/69)),
       "Patrick McCaw" : ((229/57)),
       "Kevon Looney" : ((267/66)),
       "Jordan Bell" : ((262/57)),
       "Quinn Cook" : ((312/33)),
       "Omri Casspi" : ((300/53)),
       "JaVale McGee" : ((310/65)),
       "Damian Jones" : ((25/15)),
       "Chris Boucher" : ((0))}

HOU = {
      "James Harden" : ((2191/72)),
      "PJ Tucker" : ((502/82)),
      "Trevor Ariza" : ((782/67)),
      "Eric Gordon" : ((1243/69)),
      "Clint Capela" : ((1026/74)),
      "Chris Paul" : ((1081/58)),
      "Ryan Anderson" : ((617/66)),
      "Luc Mbah a Moute" : ((460/61)),
      "Gerald Green" : ((497/41)),
      "Nene Hilario" : ((340/52)),
      "Tarik Black" : ((180/51)),
      "Joe Johnson" : ((139/23)),
      "Zhou Qi" : ((22/18)),
      "Briante Weber" : ((26/13)),
      "Bobby Brown" : ((50/20)),
      "Demetrius Jackson" : ((8/12)),
      "RJ Hunter" : ((19/5)),
      "Aaron Jackson"  : ((8/1)),
      "Markel Brown" : ((5/4)),
      "Chinanu Onuaku" : ((4/1)),
      "Troy Williams" : ((5/4)),
      "Brandan Wright" : ((4/1)),
      "Tim Quarterman" : ((4/3)),
      "Isaiah Canaan" : ((0))}

MIL = {
        "Khris Middleton" : ((1652/82)),
        "Giannis Antetokounmpo" : ((2014/75)),
        "Eric Bledsoe" : ((1266/71)),
        "Tony Snell" : ((516/75)),
        "John Henson" : ((665/76)),
        "Malcolm Brogdon" : ((625/48)),
        "Thon Maker" : ((356/74)),
        "Jason Terry" : ((166/51)),
        "Sterling Brown" : ((217/54)),
        "Jabari Parker" : ((391/31)),
        "Matthew Dellavedova" : ((164/38)),
        "DeAndre Liggins" : ((57/31)),
        "Tyler Zeller" : ((141/24)),
        "Brandon Jennings" : ((73/14)),
        "Sean Kilpatrick" : ((93/23)),
        "Rashad Vaughn" : ((59/22)),
        "Mirza Teletovic" : ((71/10)),
        "Shabazz Muhammad" : ((94/11)),
        "Gary Payton" : ((30/12)),
        "Greg Monroe" : ((34/5)),
        "DJ Wilson" : ((21/22)),
        "Marshall Plumlee" : ((14/8)),
        "Joel Bolomboy" : ((9/6)),
        "Xavier Munford" : ((3/6))}

LAC = {
        "Lou Williams" : ((1782/79)),
        "DeAndre Jordan" : ((927/77)),
        "Austin Rivers" : ((920/61)),
        "Wesley Johnson" : ((403/74)),
        "Montrezl Harrell" : ((836/76)),
        "Sindarius Thornwell" : ((202/73)),
        "Blake Griffin" : ((746/33)),
        "Milos Teodosic" : ((429/45)),
        "Tobias Harris" : ((618/32)),
        "Sam Dekker" : ((303/73)),
        "Tyrone Wallace" : ((291/30)),
        "Jawun Evans" : ((231/48)),
        "CJ Williams" : ((209/38)),
        "Danilo Gallinari" : ((321/21)),
        "Willie Reed" : ((193/39)),
        "Patrick Beverley" : ((134/11)),
        "Jamil Wilson" : ((105/15)),
        "Boban Marjanovic" : ((117/20)),
        "Avery Bradley" : ((55/6)),
        "Sean Kilpatrick" : ((19/4)),
        "Brice Johnson" : ((16/9))}

TOR = {
        "DeMar DeRozan" : ((1840/80)),
        "Kyle Lowry" : ((1267/78)),
        "Serge Ibaka" : ((959/76)),
        "Jonas Valanciunas" : ((980/77)),
        "Pascal Siakam" : ((589/81)),
        "Jakob Poetl" : ((567/82)),
        "Fred VanVleet" : ((656/76)),
        "OG Anunoby" : ((438/74)),
        "Delon Wright" : ((555/69)),
        "CJ Miles" : ((699/70)),
        "Norman Powell" : ((385/70)),
        "Lucas Nogueira" : ((122/49)),
        "Lorenzo Brown" : ((32/14)),
        "Malcolm Miller" : ((38/15)),
        "Alfonzo McKinnie" : ((21/14)),
        "Bruno Caboclo" : ((0)),
        "Nigel Hayes" : ((3)),
        "Malachi Richardson" : ((2))}

CHA = {
        "Kemba Walker" : ((1770/80)),
        "Dwight Howard" : ((1347/81)),
        "Marvin Williams" : ((744/78)),
        "Nicolas Batum" : ((740/64)),
        "Jeremy Lamb" : ((1033/80)),
        "Michael Kidd-Gilchrist" : ((681/74)),
        "Frank Kaminsky" : ((873/79)),
        "Treveon Graham" : ((273/63)),
        "Malik Monk" : ((421/63)),
        "Michael Carter-Williams" : ((239/52)),
        "Dwayne Bacon" : ((175/53)),
        "Cody Zeller" : ((233/33)),
        "Johnny O'Bryant" : ((171/36)),
        "Willy Hernangomez" : ((135/22)),
        "Julyan Stone" : ((19/23)),
        "Marcus Paige" : ((12/5)),
        "Mangok Mathiang" : ((8/4))}

BOS = {
        "Jayson Tatum" : ((1112/80)),
        "Al Horford" : ((927/72)),
        "Jaylen Brown" : ((1017/70)),
        "Terry Rozier" : ((900/80)),
        "Kyrie Irving" : ((1466/60)),
        "Marcus Smart" : ((550/54)),
        "Aron Baynes" : ((482/81)),
        "Marcus Morris" : ((734/54)),
        "Semi Ojeleye" : ((195/73)),
        "Daniel Theis" : ((331/63)),
        "Shane Larkin" : ((231/54)),
        "Abdel Nader" : ((146/48)),
        "Greg Monroe" : ((265/26)),
        "Guerschon Yabusele" : ((79/33)),
        "Jabari Bird" : ((39/13)),
        "Kadeem Allen" : ((19/18)),
        "Jonathan Gibson" : ((34/4)),
        "Xavier Silas" : ((0)),
        "Jarell Eddie" : ((0)),
        "Gordan Hayward" : ((2))}

BKN = {
        "Spencer Dinwiddie" : ((1007/80)),
        "Allen Crabbe" : ((990/75)),
        "DeMarre Carroll" : ((983/73)),
        "Joe Harris" : ((846/78)),
        "Rondae Hollis-Jefferson" : ((946/68)),
        "Caris LeVert" : ((858/71)),
        "Jarrett Allen" : ((587/72)),
        "Quincy Acy" : ((411/70)),
        "D'Angelo Russell" : ((743/48)),
        "Tyler Zeller" : ((300/42)),
        "Nik Stauskas" : ((177/35)),
        "Dante Cunningham" : ((164/22)),
        "Trevor Booker" : ((181/18)),
        "Timofey Mozgov" : ((131/31)),
        "Jahlil Okafor" : ((166/26)),
        "Sean Kilpatrick" : ((79/16)),
        "Isaiah Whitehead" : ((100/16)),
        "Milton Doyle" : ((34/10)),
        "James Webb" : ((16/10)),
        "Jacob Wiley" : ((4/5)),
        "Jeremy Lin" : ((18)),
        "Rashad Vaughn" : ((0))}

SAS = {
     "LaMarcus Aldridge" : ((1735/75)),
     "Patty Mills" : ((819/82)),
     "Kyle Anderson" : ((585/74)),
     "Pau Gasol" : ((775/77)),
     "Danny Green" : ((600/70)),
     "Dejounte Murray" : ((654/81)),
     "Bryn Forbes" : ((555/80)),
     "Manu Ginobili" : ((576/65)),
     "Rudy Gay" : ((655/57)),
     "Davis Bertans" : ((456/77)),
     "Tony Parker" : ((421/55)),
     "Brandon Paul" : ((147/64)),
     "Joffrey Lauvergne" : ((226/55)),
     "Kawhi Leonard" : ((146/9)),
     "Derrick White" : ((54/17)),
     "Darrun Hilliard" : ((16/15)),
     "Matt Costello" : ((1))}

DEN = {
    "Gary Harris" : ((1170/67)),
    "Will Barton" : ((1268/81)),
    "Nikola Jokic" : ((1385/75)),
    "Wilson Chandler" : ((738/74)),
    "Jamal Murray" : ((1352/81)),
    "Paul Millsap" : ((555/38)),
    "Devin Harris" : ((222/27)),
    "Mason Plumlee" : ((524/74)),
    "Trey Lyles" : ((724/73)),
    "Emmanuel Mudiay" : ((359/42)),
    "Torrey Craig" : ((163/39)),
    "Kenneth Faried" : ((188/32)),
    "Juan Hernangomez" : ((82/25)),
    "Malik Beasley" : ((196/62)),
    "Monte Morris" : ((10/3)),
    "Richard Jefferson" : ((30/20)),
    "Darrell Arthur" : ((54/19)),
    "Tyler Lydon" : ((0))}

OKC = {
    "Russell Westbrook" : ((2028/82)),
    "Paul George" : ((1737/79)),
    "Carmelo Anthony" : ((1261/78)),
    "Steven Adams" : ((1056/76)),
    "Jerami Grant" : ((682/81)),
    "Raymond Felton" : ((565/82)),
    "Patrick Patterson" : ((318/82)),
    "Alex Abrines" : ((353/74)),
    "Andre Roberson" : ((353/75)),
    "Josh Huestis" : ((159/69)),
    "Terrance Ferguson" : ((189/61)),
    "Corey Brewer" : ((182/18)),
    "Dakari Johnson" : ((55/31)),
    "Nick Collison" : ((31/15)),
    "Kyle Singler" : ((23/12)),
    "Daniel Hamilton" : ((2)),
    "PJ Dozier" : ((1))}

POR = {
    "CJ McCollum" : ((1732/81)),
    "Damian Lillard" : ((1962/73)),
    "Jusuf Nurkic" : ((1132/79)),
    "Al-Farouq Aminu" : ((644/69)),
    "Evan Turner" : ((649/79)),
    "Shabazz Napier" : ((644/74)),
    "Pat Connaughton" : ((441/82)),
    "Ed Davis" : ((414/78)),
    "Maurice Harkless" : ((385/59)),
    "Zach Collins" : ((292/66)),
    "Noah Vonleh" : ((119/33)),
    "Meyers Leonard" : ((112/33)),
    "Caleb Swanigan" : ((61/27)),
    "Jake Layman" : ((34/35)),
    "Wade Baldwin" : ((38/7)),
    "Georgios Papagiannis" : ((2))}

UTA = {
    "Donovan Mitchell" : ((1616/79)),
    "Joe Ingles" : ((940/82)),
    "Ricky Rubio" : ((1008/77)),
    "Derrick Favors" : ((944/77)),
    "Rudy Gobert" : ((756/56)),
    "Royce O'Neale" : ((343/69)),
    "Jonas Jerebko" : ((429/74)),
    "Rodney Hood" : ((655/39)),
    "Alec Burks" : ((494/64)),
    "Ekpe Udoh" : ((162/63)),
    "Thabo Sefolosha" : ((312/38)),
    "Jae Crowder" : ((319/27)),
    "Joe Johnson" : ((233/32)),
    "Raul Neto" : ((183/41)),
    "Dante Exum" : ((113/14)),
    "Georges Niang" : ((1)),
    "Tony Bradley" : ((8/9)),
    "Nate Wolters" : ((2/5)),
    "David Stockton" : ((10/3)),
    "Erick McCree" : ((0)),
    "Naz Mitrou-Long" : ((3))}

MIN = {
    "Andrew Wiggins" : ((1452/82)),
    "Karl-Anthony Towns" : ((1743/82)),
    "Taj Gibson" : ((999/82)),
    "Jeff Teague" : ((994/70)),
    "Jimmy Butler" : ((1307/59)),
    "Jamal Crawford" : ((822/80)),
    "Tyus Jones" : ((416/82)),
    "Nemanja Bjelica" : ((454/67)),
    "Gorgui Dieng" : ((470/79)),
    "Shabazz Muhammad" : ((120/32)),
    "Marcus Georges-Hunt" : ((59/42)),
    "Aaron Brooks" : ((75/32)),
    "Derrick Rose" : ((52/9)),
    "Cole Aldrich" : ((12/21)),
    "Justin Patton" : ((2)),
    "Anthony Brown" : (3)}

PHI = {
       "Ben Simmons" : ((1279/81)),
       "Robert Covington" : ((1009/80)),
       "Dario Saric" : ((1141/78)),
       "JJ Redick" : ((1198/70)),
       "Joel Embiid" : ((1445/63)),
       "TJ McConnell" : ((478/76)),
       "Amir Johnson" : ((342/78)),
       "Jerryd Bayless" : ((307/39)),
       "Timothe Luwawu-Cabarrot" : ((299/52)),
       "Richaun Holmes" : ((311/42)),
       "Marco Belinelli" : ((380/28)),
       "Ersan Ilyasova" : ((249/23)),
       "Justin Anderson" : ((236/38)),
       "Trevor Booker" : ((156/33)),
       "Markelle Fultz" : ((100/14)),
       "Furkan Korkmaz" : ((23/14)),
       "James Young" : ((17/6)),
       "Nik Stauskas" : ((4/6)),
       "Jahlil Okafor" : ((10/2)),
       "James Michael McAdoo" : ((8/3)),
       "Demetrius Jackson" : ((8/3)),
       "Larry Drew" : ((2/3)),
       "Jacob Pullen" : ((2/3))}

NYK = {
        "Courtney Lee" : ((913/76)),
        "Tim Hardaway" : ((996/57)),
        "Enes Kanter" : ((1000/71)),
        "Frank Ntilikina" : ((463/78)),
        "Michael Beasley" : ((976/74)),
        "Kristaps Porzingis" : ((1088/48)),
        "Jarrett Jack" : ((466/62)),
        "Kyle O'Quinn" : ((550/77)),
        "Lance Thomas" : ((298/73)),
        "Doug McDermott" : ((395/55)),
        "Trey Burke" : ((461/36)),
        "Emmanuel Mudiay" : ((194/22)),
        "Damyean Dotson" : ((182/44)),
        "Ron Baker" : ((71/29)),
        "Luke Kornet" : ((134/20)),
        "Troy Williams" : ((128/17)),
        "Isaiah Hicks" : ((80/18)),
        "Willy Hernangomez" : ((111/26)),
        "Ramon Sessions" : ((48/13)),
        "Joakim Noah" : ((12/7)),
        "Mindaugas Kuzminkas" : ((0))}

IND = {
        "Thaddeus Young" : ((955/81)),
        "Victor Oladipo" : ((1735/75)),
        "Bojan Bogdanovic" : ((1141/80)),
        "Cory Joseph" : ((649/82)),
        "Darren Collison" : ((855/69)),
        "Lance Stephenson" : ((757/82)),
        "Myles Turner" : ((828/65)),
        "Domantas Sabonis" : ((861/74)),
        "Joe Young" : ((207/53)),
        "Al Jefferson" : ((252/36)),
        "TJ Leaf" : ((156/53)),
        "Glenn Robinson" : ((95/23)),
        "Trevor Booker" : ((91/17)),
        "Damien Wilkins" : ((33/19)),
        "Alex Poythress" : ((26/25)),
        "Ike Anigbogu" : ((13/11)),
        "Ben Moore" : ((0)),
        "Edmond Sumner" : ((2/1)),
        "Trey McKinney-Jones" : ((0))}

DET = {
        "Andre Drummond" : ((1171/78)),
        "Ish Smith" : ((894/82)),
        "Stanley Johnson" : ((599/69)),
        "Anthony Tolliver" : ((703/79)),
        "Reggie Bullock" : ((698/62)),
        "Tobias Harris" : ((868/48)),
        "Luke Kennard" : ((558/73)),
        "Avery Bradley" : ((601/40)),
        "Reggie Jackson" : ((656/45)),
        "Langston Galloway" : ((360/58)),
        "Blake Griffin" : ((496/25)),
        "Eric Moreland" : ((143/67)),
        "James Ennis" : ((202/27)),
        "Dwight Buycks" : ((215/29)),
        "Henry Ellenson" : ((151/38)),
        "Boban Marjanovic" : ((118/19)),
        "Jon Leuer" : ((43/8)),
        "Jameer Nelson" : ((26/7)),
        "Willie Reed" : ((2/3)),
        "Luis Montero" : (0),
        "Reggie Hearn" : ((1)),
        "Kay Felder" : ((1))}

CHI = {
        "Justin Holiday" : ((876/72)),
        "Denzel Valentine" : ((783/77)),
        "Lauri Markkanen" : ((1033/68)),
        "Robin Lopez" : ((756/64)),
        "Jerian Grant" : ((619/74)),
        "David Nwaba" : ((555/70)),
        "Bobby Portis" : ((964/73)),
        "Kris Dunn" : ((699/52)),
        "Cristiano Felicio" : ((308/55)),
        "Paul Zipser" : ((218/54)),
        "Zach LaVine" : ((401/24)),
        "Nikola Mirotic" : ((420/25)),
        "Cameron Payne" : ((221/25)),
        "Noah Vonleh" : ((145/21)),
        "Antonio Blakeney" : ((151/19)),
        "Ryan Arcidiacono" : ((48/24)),
        "Sean Kilpatrick" : ((139/9)),
        "Quincy Pondexter" : ((45/23)),
        "Kay Felder" : ((55/14)),
        "Omer Asik" : ((1)),
        "Jarell Eddie" : ((0))}

CLE = {
      "LeBron James" : ((2251/82)),
      "JR Smith" : ((662/80)),
      "Jeff Green" : ((846/78)),
      "Kevin Love" : ((1039/59)),
      "Kyle Korver" : ((672/73)),
      "Jae Crowder" : ((454/53)),
      "Tristan Thompson" : ((307/53)),
      "Dwyane Wade" : ((513/46)),
      "Jose Calderon" : ((255/57)),
      "Cedi Osman" : ((238/61)),
      "George Hill" : ((226/24)),
      "Jordan Clarkson" : ((353/28)),
      "Channing Frye" : ((212/44)),
      "Rodney Hood" : ((227/21)),
      "Larry Nance" : ((213/24)),
      "Isaiah Thomas" : ((221/15)),
      "Derrick Rose" : ((157/16)),
      "Iman Shumpert" : ((62/14)),
      "Ante Zizic" : ((119/32)),
      "John Holland" : ((54/24)),
      "London Perrantes" : ((7/14)),
      "Kendrick Perkins" : ((3/1))}

ORL = {
        "Jonathon Simmons" : ((962/69)),
        "Aaron Gordon" : ((1022/58)),
        "Evan Fournier" : ((1013/57)),
        "DJ Augustin" : ((766/75)),
        "Nikola Vucevic" : ((939/57)),
        "Mario Hezonja" : ((722/75)),
        "Bismack Biyombo" : ((468/82)),
        "Shelvin Mack" : ((473/69)),
        "Elfrid Payton" : ((573/44)),
        "Wesley Iwundu" : ((229/62)),
        "Arron Afflalo" : ((179/53)),
        "Marreese Speights" : ((402/52)),
        "Terrence Ross" : ((209/24)),
        "Khem Birch" : ((178/42)),
        "Jonathan Isaac" : ((145/27)),
        "Rodney Purvis" : ((96/16)),
        "Jamel Artis" : ((77/15)),
        "Adeian Payne" : ((21/5)),
        "Rashad Vaughn" : ((1))}

MIA = {
        "Josh Richardson" : ((1045/81)),
        "Goran Dragic" : ((1296/75)),
        "Tyler Johnson" : ((843/72)),
        "Wayne Ellington" : ((864/77)),
        "James Johnson" : ((788/73)),
        "Kelly Olynyk" : ((872/76)),
        "Justise Winslow" : ((529/68)),
        "Bam Adebayo" : ((477/69)),
        "Hassan Whiteside" : ((754/54)),
        "Dion Waiters" : ((429/30)),
        "Dwyane Wade" : ((252/21)),
        "Rodney McGruder" : ((91/18)),
        "Jordan Mickey" : ((93/23)),
        "Derrick Jones" : ((52/14)),
        "Derrick Walton" : ((29/16)),
        "Luke Babbitt" : ((33/13)),
        "Okaro White" : ((20/6)),
        "Udonis Haslem" : ((8/14)),
        "Matt Williams" : ((5/3))}

WAS = {
        "Bradley Beal" : ((1857/82)),
        "Otto Porter" : ((1134/77)),
        "Kelly Oubre" : ((953/81)),
        "Marcin Gortat" : ((690/82)),
        "Markieff Morris" : ((841/73)),
        "Tomas Satoransky" : ((524/73)),
        "John Wall" : ((797/41)),
        "Mike Scott" : ((668/76)),
        "Ian Mahinmi" : ((366/77)),
        "Jodie Meeks" : ((487/77)),
        "Tim Frazier" : ((176/59)),
        "Jason Smith" : ((113/33)),
        "Ramon Sessions" : ((88/15)),
        "Chris McCullough" : ((46/19)),
        "Devin Robinson" : ((2))}

ATL = {
        "Taurean Waller-Prince" : ((1158/82)),
        "Dennis Schroder" : ((1301/67)),
        "Kent Bazemore" : ((836/65)),
        "John Collins" : ((777/74)),
        "Dewayne Dedmon" : ((617/62)),
        "Marco Belinelli" : ((591/52)),
        "Ersan Ilyasova" : ((501/46)),
        "Isaiah Taylor" : ((445/67)),
        "Mike Muscala" : ((405/53)),
        "Malcolm Delaney" : ((338/54)),
        "Tyler Dorsey" : ((405/56)),
        "Miles Plumlee" : ((237/55)),
        "Luke Babbitt" : ((226/37)),
        "Tyler Cavanaugh" : ((183/39)),
        "Deandre' Bembry" : ((136/26)),
        "Damion Lee" : ((161/15)),
        "Josh Magette" : ((46/18)),
        "Andrew White" : ((69/15)),
        "Jaylen Morris" : ((28/6)),
        "Antonius Cleveland" : ((13/4)),
        "Nicolas Brussino" : ((0)),
        "Jeremy Evans" : (2)}

SAC = {
        "Bogdan Bogdanovic" : ((917/78)),
        "Willie Cauley-Stein" : ((932/73)),
        "De'Aaron Fox" : ((844/73)),
        "Buddy Hield" : ((1079/80)),
        "Garrett Temple" : ((547/65)),
        "Zach Randolph" : ((857/59)),
        "Justin Jackson" : ((453/68)),
        "Kosta Koufos" : ((477/71)),
        "Skal Labissiere" : ((523/60)),
        "George Hill" : ((441/43)),
        "Vince Carter" : ((313/58)),
        "Frank Mason" : ((413/52)),
        "JaKarr Sampson" : ((103/22)),
        "Malachi Richardson" : ((87/25)),
        "Georgios Papagiannis" : ((34/16)),
        "Nigel Hayes" : ((18/5)),
        "Bruno Caboclo" : ((26/10)),
        "Jack Cooley" : ((40/7))}

LAL = {
      "Kentavious Caldwell-Pope" : ((992/74)),
      "Kyle Kuzma" : ((1242/77)),
      "Julius Randle" : ((1323/82)),
      "Brandon Ingram" : ((949/59)),
      "Lonzo Ball" : ((528/52)),
      "Brook Lopez" : ((961/74)),
      "Josh Hart" : ((496/63)),
      "Jordan Clarkson" : ((771/53)),
      "Larry Nance" : ((360/42)),
      "Corey Brewer" : ((198/54)),
      "Tyler Ennis" : ((224/54)),
      "Alex Caruso" : ((134/37)),
      "Isaiah Thomas" : ((265/17)),
      "Ivica Zubac" : ((161/43)),
      "Travis Wear" : ((75/17)),
      "Andrew Bogut" : ((36/24)),
      "Channing Frye" : ((52/9)),
      "Gary Payton" : ((39/11)),
      "Thomas Bryant" : ((22/15)),
      "Andre Ingram" : (24/2),
      "Vander Blue" : ((3/5)),
      "Luol Deng" : ((2/1)),
      "Nigel Hayes" : ((3/2)),
      "Derrick Williams" : ((1))}

NOP = {
       "Jrue Holiday" : ((1537/81)),
       "Anthony Davis" : ((2110/75)),
       "E'Twaun Moore" : ((1022/82)),
       "Darius Miller" : ((637/82)),
       "DeMarcus Cousins" : ((1210/48)),
       "Rajon Rondo" : ((537/65)),
       "Ian Clark" : ((551/74)),
       "Dante Cunningham" : ((253/51)),
       "Jameer Nelson" : ((221/43)),
       "Nikola Mirotic" : ((439/30)),
       "Cheick Diallo" : ((254/52)),
       "Emeka Okafor" : ((114/26)),
       "Tony Allen" : ((103/22)),
       "DeAndre Liggins" : ((44/27)),
       "Solomon Hill" : ((29/12)),
       "Omer Asik" : ((18/14)),
       "Larry Drew" : ((15/7)),
       "Jordan Crawford" : ((33/5)),
       "Charles Cooke" : ((6/13)),
       "Walt Lemon" : ((17/5)),
       "Jalen Jones" : ((5/4)),
       "Mike James" : ((4/4)),
       "Josh Smith" : ((2/3))}

MEM = {
        "Marc Gasol" : ((1258/73)),
        "Dillon Brooks" : ((898/82)),
        "Jarell Martin" : ((565/73)),
        "Tyreke Evans" : ((1010/52)),
        "JaMychal Green" : ((569/55)),
        "Mario Chalmers" : ((507/66)),
        "Andrew Harrison" : ((533/56)),
        "Ben McLemore" : ((422/56)),
        "James Ennis" : ((310/45)),
        "Deyonta Davis" : ((360/62)),
        "Wayne Selden" : ((325/35)),
        "Chandler Parsons" : ((284/36)),
        "Kobi Simmons" : ((196/32)),
        "Ivan Rabb" : ((201/36)),
        "Myke Henry" : ((107/20)),
        "Mike Conley" : ((205/12)),
        "Brandan Wright" : ((135/27)),
        "MarShon Brooks" : ((141/7)),
        "Briante Weber" : ((24/5)),
        "Xavier Rathan-Mayes" : ((29/5)),
        "Omari Johnson" : ((22/4)),
        "Marquis Teague" : ((11/3)),
        "Brice Johnson" : ((27/9)),
        "Vince Hunter" : ((6/4))}

DAL = {
       "Harrison Barnes" : ((1452/77)),
       "Yogi Ferrell" : ((838/82)),
       "Wesley Matthews" : ((802/63)),
       "Dennis Smith" : ((1048/69)),
       "Dirk Nowitzki" : ((927/77)),
       "Dwight Powell" : ((671/79)),
       "JJ Barea" : ((801/69)),
       "Maxi Kleber" : ((386/72)),
       "Devin Harris" : ((373/44)),
       "Salah Mejri" : ((214/61)),
       "Doug McDermott" : ((235/26)),
       "Kyle Collinsworth" : ((101/32)),
       "Nerlens Noel" : ((131/30)),
       "Dorian Finney-Smith" : ((123/21)),
       "Aaron Harrison" : ((60/9)),
       "Johnathan Motley" : ((96/11)),
       "Jalen Jones" : ((69/12)),
       "Antonius Cleveland" : ((10/13)),
       "Gian Clavell" : ((20/7)),
       "Jeff Withey" : ((15/9)),
       "Jameel Warney" : ((17/3)),
       "Scotty Hopson" : ((1)),
       "Josh McRoberts" : ((0))}

PHX = {
        "TJ Warren" : ((1271/65)),
        "Dragan Bender" : ((531/82)),
        "Josh Jackson" : ((1012/77)),
        "Devin Booker" : ((1346/54)),
        "Tyler Ulis" : ((554/71)),
        "Troy Daniels" : ((703/79)),
        "Marquese Chriss" : ((556/72)),
        "Alex Len" : ((587/69)),
        "Tyson Chandler" : ((300/46)),
        "Jared Dudley" : ((152/48)),
        "Mike James" : ((332/32)),
        "Elfrid Payton" : ((224/19)),
        "Greg Monroe" : ((225/20)),
        "Isaiah Canaan" : ((172/19)),
        "Danuel House" : ((152/23)),
        "Shaquille Harrison" : ((152/23)),
        "Davon Reed" : ((63/21)),
        "Alec Peters" : ((82/20)),
        "Josh Gray" : ((32/5)),
        "Eric Bledsoe" : ((47/3)),
        "Alan Williams" : ((20/5)),
        "Derrick Jones" : ((9/6))}

#COLLEGE DATA






UNC = {
    "Luke Maye" : ((627/37)),
    "Joel Berry" : ((617/36)),
    "Kenny Williams" : ((422/37)),
    "Theo Pinson" : ((380/37)),
    "Cameron Johnson" : ((323/26)),
    "Sterling Manley" : ((200/37)),
    "Garrison Brooks" : ((167/37)),
    "Andrew Platek" : ((71/35)),
    "Jalek Felton" : ((63/22)),
    "Brandon Robinson" : ((61/35)),
    "Brandon Huffman" : ((47/29)),
    "Seventh Woods" : ((22/20)),
    "Shea Rush" : ((7/20)),
    "Aaron Robinson" : ((6/21)),
    "Walker Miller" : ((5/20)),
    "Kane Ma" : ((2/12))}

CLEM = {
    "Marcquise Reed" : ((553/35)),
    "Gabe DeVoe" : ((497/35)),
    "Shelton Mitchell" : ((404/33)),
    "Elijah Thomas" : ((373/35)),
    "Donte Grantham" : ((269/19)),
    "Aamir Simms" : ((135/34)),
    "Mark Donnal" : ((126/34)),
    "David Skara" : ((85/26)),
    "Clyde Trapp" : ((53/29)),
    "Anthony Oliver II" : (40/19),
    "Malik William" : ((25/17)),
    "Scott Spencer" : ((24/19)),
    "Lyles Davis" : (0),
    "Isaac Fields" : (0)}

DUKE = {
    "Marvin Bagley III" : ((694/33)),
    "Grayson Allen" : ((572/37)),
    "Gary Trent Jr" : ((536/37)),
    "Wendell Carter Jr" : ((501/37)),
    "Trevon Duval" : ((380/37)),
    "Alex O'Connell" : ((120/36)),
    "Marques Bolden" : ((112/29)),
    "Javin DeLaurier" : ((112/33)),
    "Jordan Goldwire" : ((1)),
    "Justin Robinson" : ((23/17)),
    "Jack White" : ((22/28)),
    "Antonio Vrankovic" : ((1)),
    "Jordan Tucker" : ((3)),
    "Mike Buckmire" : ((3/4))}

NCS = {
    "Allerik Freeman" : ((530/33)),
    "Torin Dorn" : ((458/33)),
    "Omer Yurtseven" : ((445/33)),
    "Braxton Beverly" : ((294/31)),
    "Lennard Freeman" : ((261/33)),
    "Markell Johnson" : ((231/26)),
    "Sam Hunt" : ((182/33)),
    "Abdul-Malik Abu" : ((141/27)),
    "Lavar Batts Jr" : ((112/30)),
    "Darius Hicks" : ((17/4)),
    "Shaun Kirk" : ((11/5)),
    "Spencer Newman" : ((0))} 


#Add a button to select a team
teamvar = StringVar(window)
teamvar.set("Select Team...")

#Create a function for team selection
if teamvar.get() == "Denver Nuggets": DEN
if teamvar.get() == "Oklahoma City Thunder" : OKC
if teamvar.get() == "Portland Trail Blazers" : POR
if teamvar.get() == "Utah Jazz" : UTA
if teamvar.get() == "Minnesota Timberwolves" : MIN
if teamvar.get() == "Atlanta Hawks": ATL
if teamvar.get() == "Boston Celtics" : BOS
if teamvar.get() == "Brooklyn Nets" : BKN
if teamvar.get() == "Charlotte Hornets" : CHA
if teamvar.get() == "Chicago Bulls" : CHI
if teamvar.get() == "Cleveland Cavaliers": CLE
if teamvar.get() == "Dallas Mavericks" : DAL
if teamvar.get() == "Detroit Pistons" : DET
if teamvar.get() == "Golden State Warriors" : GSW
if teamvar.get() == "Houston Rockets" : HOU
if teamvar.get() == "Indiana Pacers": IND
if teamvar.get() == "LA Clippers" : LAC
if teamvar.get() == "LA Lakers" : LAL
if teamvar.get() == "Memphis Grizzlies" : MEM
if teamvar.get() == "Miami Heat" : MIA
if teamvar.get() == "Milwaukee Bucks": MIL
if teamvar.get() == "New Orleans Pelicans" : NOP
if teamvar.get() == "New York Knicks" : NYK
if teamvar.get() == "Philadelphia 76ers" : PHI
if teamvar.get() == "Phoenix Suns" : PHX
if teamvar.get() == "Sacramento Kings": SAC
if teamvar.get() == "San Antonio Spurs" : SAS
if teamvar.get() == "Toronto Raptors" : TOR
if teamvar.get() == "Washington Wizards" : WAS
if teamvar.get() == "Orlando Magics" : ORL
    
#Start the first label for the window
labelone = Label(window, 
text="Welcome to Basketball DataVis!", 
font = ("Arial Bold", 31),
relief=RAISED)
labelone.configure(background="grey")
labelone.grid(column=0, 
row=0, 
columnspan=16, 
rowspan=10, 
sticky=NW)

#Add the first image that goes witht the first label
base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'mj.gif')
mjgif = PhotoImage(file=image_path)
mjimg = Label(image=mjgif)
mjimg.image = mjgif
mjimg.grid(column=1, row=10, sticky=N)

#Create a variable for the checkbox to flip between NBA and College data
dt_chk = IntVar()
dt_chk.set(0)

#Create a second label that shows whether we will display data from NCAA bball or NBA bball
datatype_label = Label(window, 
text="NBA Data", 
font = ("Arial", 28),
relief=GROOVE)
datatype_label.configure(background="grey")
datatype_label.grid(column=0, 
row=10, 
rowspan=2, 
sticky=NW)

def dtchk_flip():
    if dt_chk.get() == 0:
        datatype_label.configure(text="NBA Data")
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'mj.gif')
        mjgif = PhotoImage(file=image_path)
        mjimg = Label(image=mjgif)
        mjimg.image = mjgif
        mjimg.grid(column=1, row=10, sticky=N)

    elif dt_chk.get() == 1:
        datatype_label.configure(text="College Data")
        base_folder2 = os.path.dirname(__file__)
        image_path2 = os.path.join(base_folder2, 'mjunc.gif')
        mjuncgif = PhotoImage(file=image_path2)
        mjuncimg = Label(image=mjuncgif)
        mjuncimg.image = mjuncgif
        mjuncimg.grid(column=1, row=10, sticky=N)

#Add a checkbox to the window to decide what data to display
datatype = Checkbutton(window, 
text="College Basketball", 
font = ("Arial", 14),
relief=GROOVE, 
var=dt_chk, 
onvalue=1, 
offvalue=0, 
command=dtchk_flip)
datatype.configure(background="grey")
datatype.grid(column=11, row=10, sticky= NW)

#Add a button to exit the window
def quitwindow():
    window.destroy()

quitbutton = Button(window, 
text="Quit", 
command=quitwindow)
quitbutton.configure(background = "black")
quitbutton.grid(column=11, 
row=10, 
pady=180, 
sticky=E)


#Define a search variable
searchvar = "Player 1"

#Add a entry box to use to search
searchbox = Entry(window, textvariable=searchvar, relief=RAISED, width=18)
searchbox.configure(background="grey")
searchbox.grid(column=11,
row=10,
padx=5,
pady=75,
sticky=NW)

#Create the search function
def searchdata():
    if dt_chk.get() == 0:
        if teamvar.get() == "Denver Nuggets":
            if searchbox.get() in DEN:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = DEN.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Oklahoma City Thunder":
            if searchbox.get() in OKC:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = OKC.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Portland Trail Blazers":
            if searchbox.get() in POR:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = POR.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Utah Jazz":
            if searchbox.get() in UTA:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = UTA.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Minnesota Timberwolves":
            if searchbox.get() in MIN:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = MIN.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Atlanta Hawks":
            if searchbox.get() in ATL:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = ATL.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Milwaukee Bucks":
            if searchbox.get() in MIL:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = MIL.get(searchresult))
                    searchres.pack()
                    mainloop()  
        if teamvar.get() == "New Orleans Pelicans":
            if searchbox.get() in NOP:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = NOP.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "New York Knicks":
            if searchbox.get() in NYK:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = NYK.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Orlando Magic":
            if searchbox.get() in ORL:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = ORL.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Philadelphia 76ers":
            if searchbox.get() in PHI:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = PHI.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Phoenix Suns":
            if searchbox.get() in PHX:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = PHX.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Sacramento Kings":
            if searchbox.get() in SAC:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = SAC.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "San Antonio Spurs":
            if searchbox.get() in SAS:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = SAS.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Toronto Raptors":
            if searchbox.get() in TOR:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = TOR.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Washington Wizards":
            if searchbox.get() in WAS:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = WAS.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Boston Celtics":
            if searchbox.get() in BOS:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = BOS.get(searchresult))
                    searchres.pack()
                    mainloop()  
        if teamvar.get() == "Brooklyn Nets":
            if searchbox.get() in BKN:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = BKN.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Charlotte Hornets":
            if searchbox.get() in CHA:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = CHA.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Chicago Bulls":
            if searchbox.get() in CHI:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = CHI.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Cleveland Cavaliers":
            if searchbox.get() in CLE:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = CLE.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Dallas Mavericks":
            if searchbox.get() in DAL:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = DAL.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Detroit Pistons":
            if searchbox.get() in DET:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = DET.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Golden State Warriors":
            if searchbox.get() in GSW:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = GSW.get(searchresult))
                    searchres.pack()
                    mainloop() 
        if teamvar.get() == "Houston Rockets":
            if searchbox.get() in HOU:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = HOU.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Indiana Pacers":
            if searchbox.get() in IND:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = IND.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "LA Clippers":
            if searchbox.get() in LAC:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = LAC.get(searchresult))
                    searchres.pack()
                    mainloop()  
        if teamvar.get() == "LA Lakers":
            if searchbox.get() in LAL:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = LAL.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Memphis Grizzlies":
            if searchbox.get() in MEM:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = MEM.get(searchresult))
                    searchres.pack()
                    mainloop()
        if teamvar.get() == "Miami Heat":
            if searchbox.get() in MIA:
                    searchresult = searchbox.get()
                    result = tkinter.Tk()
                    result.title(searchbox.get())
                    result.geometry("200x75")
                    searchres = Label(result, text = MIA.get(searchresult))
                    searchres.pack()
                    mainloop()
    
#Add a search button to start the search
gosearch = Button(window, 
text = "GO", 
command = searchdata)
gosearch.configure(background = "black")
gosearch.grid(column = 11, 
row = 10, 
pady = 75)

if dt_chk.get() == 0:
    teamselect = OptionMenu(window, 
    teamvar,
    "Atlanta Hawks",
    "Boston Celtics",
    "Brooklyn Nets",
    "Charlotte Hornets",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Dallas Mavericks",
    "Denver Nuggets",
    "Detroit Pistons",
    "Golden State Warriors",
    "Houston Rockets",
    "Indiana Pacers",
    "LA Clippers",
    "LA Lakers",
    "Memphis Grizzlies",
    "Miami Heat",
    "Milwaukee Bucks",
    "Minnesota Timberwolves",
    "New Orleans Pelicans",
    "New York Knicks",
    "Oklahoma City Thunder",
    "Orlando Magic",
    "Philadelphia 76ers",
    "Phoenix Suns",
    "Portland Trail Blazers",
    "Sacramento Kings",
    "San Antonio Spurs",
    "Toronto Raptors",
    "Utah Jazz",
    "Washington Wizards")
    teamselect.configure(background = "black")
    teamselect.grid(column=11, 
    row=10, 
    pady = 30,
    sticky=NW)
if dt_chk.get() == 1:
    teamselect = OptionMenu(window, 
    teamvar, 
    "UNC",
    "CLEM",
    "DUKE",
    "NCS",
    "VT")
    teamselect.configure(background = "grey")
    teamselect.grid(column=11, 
    row=10, 
    padx=15,
    sticky=NW)

#End the main loop
window.mainloop()