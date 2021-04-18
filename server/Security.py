import rsa

# Initial Global Authentication
# Server Global
__server_public_key__ = 'PublicKey(531836556116849503526789038592954213414151379898321835881401907556007177415927997307542592331199274089794331573843691592574639966270561486557382534282742103050057822993660888083548379856155488483196639832097391417134087217005299569802699831391478549250744498375602059643144903775349274801998146688120183504125221051061736348327457268507586608176443284233413990577635177136336631459383851827187507721004587701804374282750434372917940361127765542157619677292146401841569985916480798394424532280393237433015726920840531167288665933370139294868651026141601666325426407672025889314600906028786618408177562737233790002944266034792992474306740850812523601523756217918206069415070327585539353356359071939307735577061091608639360563326396192850344390658852913223887011225691903782488742287948888014633114365077164593903473318600607600949451658093178850075458821016403433532568744679880492952441636867853655522362814535616187809821323397068788947480892419246810990841597653670945038818458829019200666865229015233677540241824247978388149314379895411043381152108020013195083056299043554246377658123133279533462604856780710681653462894342224519486425570059768811070058412378593332019844589337496030320729967749686813819445032235455418790559505833, 65537)'
__server_private_key__ = rsa.PrivateKey(531836556116849503526789038592954213414151379898321835881401907556007177415927997307542592331199274089794331573843691592574639966270561486557382534282742103050057822993660888083548379856155488483196639832097391417134087217005299569802699831391478549250744498375602059643144903775349274801998146688120183504125221051061736348327457268507586608176443284233413990577635177136336631459383851827187507721004587701804374282750434372917940361127765542157619677292146401841569985916480798394424532280393237433015726920840531167288665933370139294868651026141601666325426407672025889314600906028786618408177562737233790002944266034792992474306740850812523601523756217918206069415070327585539353356359071939307735577061091608639360563326396192850344390658852913223887011225691903782488742287948888014633114365077164593903473318600607600949451658093178850075458821016403433532568744679880492952441636867853655522362814535616187809821323397068788947480892419246810990841597653670945038818458829019200666865229015233677540241824247978388149314379895411043381152108020013195083056299043554246377658123133279533462604856780710681653462894342224519486425570059768811070058412378593332019844589337496030320729967749686813819445032235455418790559505833,65537,49404473101292091146544572790239181702936564090833931013717057741443332714469225744363020921194762968379203970605312944071202650634834953234987028223954925055598395202487258901882029030383975676117325225411735644712335367458508381234399447236085286293826884143471097839502360104739710163641373835196540536996114343941038663481965299764624368991229179157010915584122601864687388991329003309945794696209407356586127388091988410551664264744279363117866069477617029989341563914422922938572967217343394258086267993562066523436431301438231960986318376598716312076982406425489320752357424371032579443350693454551270667524113071627429326868419212187208497659589094151853937369105614411445753679378782623229570464404945263928260654645569066502318612765582479887075236769919399797031662316563881829588140276645550891994963731619432874929682089321232536985055180565821905258859611645428877092364796799610537825084626186359964430278921802443892944871243765287481031400875227812187825602898578187450661353239785758814907736535384171782695387380381738555236045474276392768636376507493425200119882438681252629074946255555416921358800497854757668592269073116935757668704753095094651507962754013924196310043516921384384300937835383665572199730026113,6865127938694791411071782745185249736677602590818394974350918303804266583465328453182830988895536410254705660080571534242206181248886444529289414291158408275258747137852070220689341689440973577344662748330354697077318988192471665089612057826856344839396349288892845092177848972937456435760053867676283828786807346039928466454567338668337896243293324078258550423406280577200285441330280853539709678114305667552130787651085483338853108294247928679259413229228829503084098168848562535234622763865452097226140036753186011203412093483386429937160333897150510966571789666038551719525440812748439252555594123108674661297893697517530358623034920378628225574527893,77469285476704907601345632814765028947714757323166228286346425048395502606393089794098708586423758905653736282516194292559624926167439481230772660075844603293245145832017564297245754743170490908868110767191789666383255293512999753435327320327344579215269307740047088263619842466676947975191618749280479249007980455012692058695711872913031047732760284053702301440183394417561671678736649609683333446754063573432357189171902723013588375288405359594742545787002194011458620623724924003214548687757653111256126748608950377856940643917162171566746524015075381307837532341607411600581)

# Client Global
__client_initial_public_key__ = rsa.PublicKey(578198453259670039019636013090940026799659645944564293448663722521623793018039481177959591072712284209107030191350694207884016489756822609577941996499949397575929296921489051038414368542686434603376664176981445526502037743840876252191278746897266370061459332403535515451811396994925733720535132744982147586068505821971873258798865594021961248329306231549388276031974828015262677359940070995907518571369799458225210240961089404564929583561051357064078611311733902099186741097402712296230704339907117604010597534325611008238031425356320128600753613520778586235115686880033809224890728375842917474778600479972380925338823045397680964467487039004687134864285191106123357959554154136661786732768518048514262122511763834578241851872618279817023789483996698601334619392788999639316353284947730052428356071935743720461619690928689688343249300613498901784439622466606845797526008676855500010629281793232911499859021035506868506620678196766766520481536598971822308178688601476112109259227361897737886178302914782615469830104071521799015954532551466951306367537884446355613003109742557088605860270464086670142943967318731686168454230523291649582084753674120426473751070138511249918778843922601863177576363717592633458441366881996258624016521969,65537)
__client_initial_private_key__ = rsa.PrivateKey(578198453259670039019636013090940026799659645944564293448663722521623793018039481177959591072712284209107030191350694207884016489756822609577941996499949397575929296921489051038414368542686434603376664176981445526502037743840876252191278746897266370061459332403535515451811396994925733720535132744982147586068505821971873258798865594021961248329306231549388276031974828015262677359940070995907518571369799458225210240961089404564929583561051357064078611311733902099186741097402712296230704339907117604010597534325611008238031425356320128600753613520778586235115686880033809224890728375842917474778600479972380925338823045397680964467487039004687134864285191106123357959554154136661786732768518048514262122511763834578241851872618279817023789483996698601334619392788999639316353284947730052428356071935743720461619690928689688343249300613498901784439622466606845797526008676855500010629281793232911499859021035506868506620678196766766520481536598971822308178688601476112109259227361897737886178302914782615469830104071521799015954532551466951306367537884446355613003109742557088605860270464086670142943967318731686168454230523291649582084753674120426473751070138511249918778843922601863177576363717592633458441366881996258624016521969,65537,577986713892927098681560250326178402669119770278869044306304933908466050505681073750883725070518941596216318551748753065308231568326879772056696431278532506574787616601576395023874155459313309888628033022973060115320017680275986479542964196491762084041631219673662545185078963811718107225436290210446243111617956603366698701553169685233696190881453822230115417667619312873093119640535176635410367642189140056864186620017453502010501423742849955831652075359958849630346536605492224097272718211397149634428586542964642171333722214464632201428523909891920098875766879695006712906443480297214332555689131221928184017116570674551815855207301001881991682881531124437591816735962198671839020860220395173900414774787352988345965981759177358679198671553072447648973752264245982460047766026046251203354769624142868913904995698528189940061956738319104707877387787182773953115228107143302093771634775705091715415478992399185959085890961981421685515321561995620812972485150637978445680775968534630789876056467588139361228435683782637966518479581859714463606997461280578156584116046650966191611237539520678188290886658995818238043314998273653112489929361709385339664790345419473777456433717110966638171541994626650899138846345266095422249598374213,10378395861299891975208895225729177902914259384182029863349146367499264960496493410865409675245610368728334360042451670157061801530765901897048815975999137754774333986237954173352347966122388342084887448984076431972480712663187885315951993596168848449685061688034407421186264746237237054232347994669463350556563855101694002045347537892364388190031333419942839800527419281900518519615434120466898271257726766074310403475035646401323398267962548654224301719725220896979621498346837669426654927445539810734951812055474446724988242143678003275928328166623450957290490760426357733598759089699431145276560498969583215206739524490972586702988359273402306595868439,55711736282455774441920112196894939000627866282745915915387274486389176865710594317238417580627083778940757304973874366531516836256537216494826287481116989092619188610713630983396051238535543471582979517311255578177375810365884629244194223966216629073115011811513725687918153762706254113624502383136601522492509532308495110968086984258584152496786309290479744034686447316012919120567688179389139075940763055775420412133799788303866532699253075888670230097111423584851849739741169747164195149856055473470700238971351428854969715949373809373527633433544909002220247077647966825271)


def get_key(key: str):
    key = key[10:-1]
    key_numeric = [i for i in map(int, key.split(','))]
    return rsa.PublicKey(key_numeric[0], key_numeric[1])


