import rsa
import pickle

if __name__ == '__main__':
    public, private_k = rsa.newkeys(1024)

    var = 'PublicKey(157137637721861869372539893459600696742127499758127772090085112140787972009214342489665530996268305128037221399721176471559193370133031726130729193098952822312718353677752558323517006429252983185444022055723152643529270527892933839066752166883567099046052682883104837595785078185695586176198813398487786120801,65537)__server_private_key__rsa.PrivateKey(153479565307109564197997366112287960436400200886230813383955527999664984402398678762266835053163840025004137309234234296442926603527018877278452833043158154349572364075989212640279342343355762948079249181852702965699899782277805411509669798247394844322618281836704853954015313872756543429415231152518292985093,65537,30463130529546381602568773950419485013911131317089436814295642281759038666805041630522712214040240338209771855875595766179861593583463716002229484562769770821410178476803304192032061593058293310795361852950195777246633869875878028465944954891549813150775103835332448661683979058570160507285165184106812114945,55537758210444071218413159150012759189767997919433615002525493775627266119765236783497321293067053544055718202682695521590801668269713670777849452295464272832468709,2763517474463835864396985967076149699473333329194721245889576736985561944189010002379589782451842891236096628798805340946302137914880219004060577)'


    def encr(msg):

        encrypted = list()
        offset = 0
        chunk_size = 116
        end_loop = False

        while not end_loop:

            chunk = msg[offset: chunk_size + offset]

            if len(chunk) % chunk_size != 0:
                end_loop = True

            print(chunk)
            enc= rsa.encrypt(chunk.encode(), public)

            offset += chunk_size

            encrypted.append(enc)
        return pickle.dumps(encrypted)

    def decr(msg):
        encrypted = pickle.loads(msg)

        decry = ''
        for chunk in encrypted:
            decry += rsa.decrypt(chunk, private_k).decode()

        return decry

    encrpy = encr(var)
    decpy = decr(encrpy)
    if decpy == var:
        print('Success')
    else:
        print(decpy)




