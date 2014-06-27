def aa():
	print("aa")
	
def bb():
	print("bb")
	
fundict = {
	"aa" : aa,
	"bb" : bb
}

fundict["aa"]()