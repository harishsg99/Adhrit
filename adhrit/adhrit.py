# !/usr/bin/env python3

# ADHRIT is an open source tool for Android apk analysis
# to extract maximum amount of information from an apk

import argparse
import configparser
from colorama import Fore, Style
from adhrit.recons.smali_extract import smali_de
from adhrit.recons.smali_extract import smali_re
from adhrit.recons.smali_extract import apk_sign
from adhrit.recons.smali_extract import inj_check
from adhrit.recons.manifest_analysis import man_analyzer
from adhrit.recons.dbaccess import dbconnection, insert_statustable
from adhrit.recons.smarser.parser import parser
from adhrit.recons.native_recon import lib_pwn
from adhrit.recons.dynamic import adb_con
from adhrit.recons.clean import cleaner
from adhrit.recons.reset import reset_db


__author__ = 'Abhishek J M ( jmabhishek4@gmail.com, @HawkSpawn )'
__version__ = "0.2"


class Adhrit:

	def __init__(self):
		self.apk_name = ""

	@staticmethod
	def welcome():
		print(Fore.RED + Style.BRIGHT)
		print("          ####  #######      ##      ##  ########    ##  ############")
		print("         ## ##  ##     ##    ##      ##  ##     ##   ##       ##")
		print("        ##  ##  ##      ##   ##      ##  ##      ##  ##       ##")
		print("       ##   ##  ##       ##  ##      ##  ##      ##  ##       ##")
		print("      ##    ##  ##       ##  ##      ##  ##     ##   ##       ##")
		print("     #########  ##       ##  ##########  ##   ##     ##       ##")
		print("    ##      ##  ##       ##  ##      ##  ##  ##      ##       ##")
		print("   ##       ##  ##       ##  ##      ##  ##   ##     ##       ##")
		print("  ##        ##  ##      ##   ##      ##  ##    ##    ##       ##")
		print(" ##         ##  ##     ##    ##      ##  ##     ##   ##       ##")
		print("##          ##  #######      ##      ##  ##      ##  ##       ##")
		print(Fore.YELLOW + Style.BRIGHT + "\n\n| Project\t\t:\t" + Fore.GREEN + "www.github.com/abhi-r3v0/Adhrit")
		print(Fore.YELLOW + Style.BRIGHT + "| Twitter\t\t:\t" + Fore.GREEN + "@0xADHRIT")
		print(Fore.YELLOW + Style.BRIGHT + "| Author\t\t:\t" + Fore.GREEN + __author__)
		print(Fore.YELLOW + Style.BRIGHT + "| Version\t\t:\t" + Fore.GREEN + __version__)




	print("\n\n")

	# # Extract the source code of the APK in smali
	# @staticmethod
	# def smaliextractor(apk_name):
	#     smali_de(apk_name)

	# # Bytecode Analysis
	# @staticmethod
	# def bytecodeanalyzer():
	#     parser()

	# # Recompile smali back into APK
	# @staticmethod
	# def smalirecompile(apk_name):
	#     smali_re(apk_name)

	# # Sign the apk with a generic signature. For educaational purposes only!
	# @staticmethod
	# def apk_signing(apk_name):
	#     apk_sign(apk_name)

	# # Check for string injection points
	# @staticmethod
	# def smali_inj(apk_name, flag_format=''):
	#     inj_check(apk_name, flag_format)

	# # Analyze native library
	# @staticmethod
	# def native_recon():
	#     lib_pwn()

	
	@staticmethod
	def cleanproject(apk_name):
		cleaner(apk_name)

	@staticmethod
	def manifestanalyzer(apk_name, hash_of_apk):
		man_analyzer(apk_name, hash_of_apk)


def main(hash_of_apk):
	adhrit = Adhrit()
	# parser = argparse.ArgumentParser(description="Android Dynamic Handling, Reversing and Instrumentation Toolkit")
	# parser.add_argument("-pen", help="Run ADHRIT in pentest mode")
	# parser.add_argument("-mal", help="Run ADHRIT in malware analysis mode")
	# parser.add_argument("-c", help="Clean up for a new project")
	# parser.add_argument("-a", help="Dump package info and extract contents")
	# parser.add_argument("-x", help="Extract APK contents only")
	# parser.add_argument("-p", help="Check for virtual apps")
	# parser.add_argument("-s", help="Source code of the APK in Smali")
	# parser.add_argument("-b", help="Recompile smali back into APK")
	# parser.add_argument("-m", help="Sign the APK")
	# parser.add_argument("-i", help="Check for injection points")
	# parser.add_argument("-pwn", help="Scan for vulnerabilities", action="store_true")
	# parser.add_argument("--flag", help="Check for CTF flags")
	# parser.add_argument("-w", help="Welcome :P", action='store_true')
	# parser.add_argument("-v", help="Check footprints in VirusTotal database")
	# parser.add_argument("-d", help="Analyse the behaviour dynamically in a VM")
	# parser.add_argument("-cr", help="Check device root status", action='store_true')
	# parser.add_argument("-l", help="Extract, parse and analyze manifest")
	# parser.add_argument("-r", help="Analyze native library", action='store_true')
	# args = parser.parse_args()

	# Adhrit Welcome ASCII
	adhrit.welcome()
	apk_name = 'app.apk'
	adhrit.manifestanalyzer(apk_name, hash_of_apk)

	#--------------------------------
	dbname = "adhrit.db"
	dbconstatus = dbconnection(dbname)
	query = f"UPDATE StatusDB SET Manifest='complete' WHERE Hash='{hash_of_apk}';"
	addedornot = insert_statustable(dbconstatus, query)
   
   


	





	# if args.pen:
	#     adhrit.cleanproject(args.pen)
	#     adhrit.apkextractor(args.pen)
	#     adhrit.native_recon()
	#     adhrit.manifestanalyzer(args.pen)
	#     adhrit.smaliextractor(args.pen)
	#     adhrit.bytecodeanalyzer()
	#     adhrit.smali_inj(args.pen)

	# if args.mal:
	#     adhrit.vtanalyzer(args.mal)
	#     adhrit.vappsearch(args.mal)

	# if args.c:
	#     adhrit.cleanproject(args.c)

	# if args.a:
	#     adhrit.cleanproject(args.a)
	#     adhrit.vtanalyzer(args.a)
	#     adhrit.apkextractor(args.a)
	#     adhrit.manifestanalyzer(args.a)
	#     adhrit.native_recon()
	#     adhrit.vappsearch(args.a)
	#     adhrit.smaliextractor(args.a)
	#     adhrit.smali_inj(args.a)
	#     adhrit.bytecodeanalyzer()

	# elif args.x:
	#     adhrit.cleanproject(args.x)
	#     adhrit.apkextractor(args.x)

	# elif args.p:
	#     adhrit.vappsearch(args.p)

	# elif args.s:
	#     adhrit.smaliextractor(args.s)

	# elif args.b:
	#     adhrit.smalirecompile(args.b)

	# elif args.m:
	#     adhrit.welcome()
	#     adhrit.apk_signing(args.m)

	# elif args.i:
	#     adhrit.smali_inj(args.i, args.flag)

	# elif args.pwn:
	#     adhrit.bytecodeanalyzer()

	# elif args.r:
	#     adhrit.native_recon()

	# elif args.w:
	#     adhrit.welcome()

	# elif args.v:
	#     adhrit.vtanalyzer(args.v)

	# elif args.d:
	#     adhrit.dynamicanalysis(args.d)

	# elif args.cr:
	#     adhrit.checkroot()

	# elif args.l:
	#     adhrit.manifestanalyzer(args.l)


# if __name__ == "__main__":
#     main(hash_key)
