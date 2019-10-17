import geometrik

def main():
    a = 50
    t = 45
    s = 30
    d1= 20
    d2= 10
    luas = geometrik.menghitungjajargenjang(a,t)
	
    print("\nMenghitung luas jajargenjang ")
    print("\nhasil : ",luas)
	
    keliling = geometrik.menghitungkelilingsiku(s)
	
    print("\nmenghitung keliling dari siku")
    print("\nHasil : ",keliling)
	
    belahketupat = geometrik.menghitungbelahketupat(d1,d2)
    print("\nMenghitung luas belahketupat")
    print("hasil : ",belahketupat)
	

	 
if __name__=="__main__":
    main()
