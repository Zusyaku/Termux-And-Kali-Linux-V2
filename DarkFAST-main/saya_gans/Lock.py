

from modul import *

class shielded:
	def __init__(
	
	
	
	
	
	
	
self












																											,
	

















url













									,
									
									
									
















         cookie











																																								,







										main_menu
																	
							
							
							
							
							
							

	

):
		
		self.url=url
		self.cookies=cookie
		self.uid=re.search(


"c_user=(\d*)"

,			cookie["cookie"]


			).group(

					1



)
		self.main=main_menu
		print("\n * thanks to \x1b[1;35mNanta XE\x1b[0m the information :)\n")
		print(" 1. On Lock Profile :( ")
		print(" 2. Off Lock Profile :)")
		print(" 3. Back\n")
		self.ngentod(




)
	
	def ngentod(



			self

):
		pilih=input(


				" ? Menu : "


)
		while pilih in (



""			


						,



" "



					):
			print(" ! Anak Pantek Lu")
			pilih=input(









" ? Menu : "













																							)
		if pilih in (











"1"












																								,











																																"01"











			):
				
				
				
				
				
				
				
				
				
				
				
				
				
			self.peler(




						





																														"true"










																												)
		elif pilih in (






"2"













																																				,
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				
																																				



																								"02"


















):
	
	
	
	
	
	
	
	
	
			self.peler(








																																		"false"



		









)
		elif pilih in (




									"3"













,


				




																	"03"














):
			kembali(










								" * mohon tunggu sebentar"









,

			
			
			
			
			
			
			
																		self.main






																			
































																					)
		else:
			
			
			
			
			
			
			
			
			
			
			
			
			
			print(
















" ! Kontol Menu Tidak Ada"







											);self.ngentod(
											
											
											
											
											
											
											
											
											
											
											
											
											
											
											
											
											
											
											)
	
	def peler(



						self

														,





																																			shield


																				,						



				





			**tytyd



					):
		try:
			
			
			
			
			
			ses=req.session()
			ses.headers.update({"content-type":"application/x-www-form-urlencoded"})
			
			
			
			
			
			
			
			
			
			
			
			respon=req.get(


















																																							"{}/composer/ocelot/async_loader/?publisher=feed".format(












								self.url













)




																							,
																							
																							
																							
																							
																							
																							
																							
																							
																				
																				
																				
																				
																				
																				
																				
																				
																				
																				
																				
																				
																				
																				
																				
								
								
								
								
								
								
								
								
								
								
								
								
								
								
								

														cookies=self.cookies




).text















			dtsg=re.search(










																																				r'"fb_dtsg\\" value=\\"(.*?)\\"'



									




																														,







											respon









).group(


				1



)
			tytyd.update(







{


																																																				"fb_dtsg":







																											dtsg
					
					
	
	
	
	
	
	
																															,
																															
																															
																															
																															
																															
																															
																															
																															
																															



										"variables":











															json.dumps(



	{





											"0":








																																	{
																																	
																																	
																																	
																																	
																																	
																																	
																																	
																																	
																																	
																																	


																																											"is_shielded":


















																								shield

















					,
					
					
					
					
					
					
					
					
					





																								"actor_id":
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									
																									






																																																												self.uid


















,







																																						"client_mutation_id":
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					
																					





																														"NGENTOD"
											
											
											
											
											
											
											
											
											
											
																				
																				
																				
																				
	
																																		}
																																		
																																		
																																		
																																		
																																		
																																		
																																		
																																		
																																		
												
											
											
											
											
											
											
											
											
																																												}



										









)














																			,
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			
																			

																																																"doc_id":




















																																																				"1477043292367183"







					}
					
					
					
					
					
														)
														
														
														
														
														
														
														
														
														
														
														
														
														
			respon=ses.post(


























																																										"https://www.facebook.com/api/graphql"











						
						
						
						
						
						
						
						
						
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										,
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										
																										










																																					data=tytyd


																										
																										
																										
																										
																										
																										
																										
																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																										
																																																																					
																										





,





						cookies=self.cookies


















								









					).text
			if '"NGENTOD","is_shielded":' in respon:
				jonson=json.loads(








															respon








					

)





				if jonson[




								"data"





][





			"is_shielded_set"
			
			
			

								][









"is_shielded"



																								] is True:
					exit(




" * Lock Profile Suksess Silahkan Cek Profile Anda.. Jika Belum Lock Profile Tunggu Hingga Berapa Menit ;)"






																						)
				if jonson[










																"data"


				





					][



			"is_shielded_set"





][




								"is_shielded"



							] is False:
					exit(









														" * sukses mematikan perisai foto profil, cek profile ente sekarang jika belum mati silahkan tunggu beberapa menit"






					)



				else:
					exit(





						" ! gagal mengaktifkan perisai foto profil" if "true" in shield else " ! gagal mematikan perisai foto profil"








)
			else:
				exit(






						" ! error tidak diketahui"

						)
		except koneksi_error: exit(" ! Jaringan Failde")
		except (KeyboardInterrupt,EOFError): exit()
		except Exception: exit(" ! Failed")
			
		
			
