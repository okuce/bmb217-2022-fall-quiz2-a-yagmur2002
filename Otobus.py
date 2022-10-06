"""yağmur bayrak 20217170058"""
 class Otobus:
    nereden:str=""
    nereye:str=""
    plaka:str=""
    bos_koltuk:int=0
    dolu_koltuk:int=0

    def init(self,nereden,nereye,plaka,bos_koltuk,dolu_koltuk) :
        self.nereden=nereden
        self.nereye=nereye
        self.plaka=plaka
        self.bos_koltuk=bos_koltuk
        self.dolu_koltuk=dolu_koltuk


    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        return self.dolu_koltuk +=1


    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        return self.bos_koltuk -= 1



    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print("Otobüs güzergahi:{}{},Plaka:{} ,Bos Koltuk:{},Dolu Koltuk:{} ",format(self.nereden,self.nereye,self.plaka,self.bos_koltuk,self.dolu_koltuk))
