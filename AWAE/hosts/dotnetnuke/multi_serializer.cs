using System;
using System.IO;
using System.Xml;
using System.Xml.Serialization;

namespace MultiXMLSerializer{
	class Program{
		static void Main(string[] args){
			int myClass = Int32.Parse(args[1]);
		}

		if(myClass == 1){
			MyFirstConsoleText myText = new MyFristConsoleText();
			myText.text = text;
			CustomSerializer(myText);
		}else{
			MySecondConsoleText myText = new MySecondConsoleText();
			myText.txt = txt;
			CustomSerializer(myText);
		}

		static void CustomSerializer(Object myObj){
			XmlDocument xmlDocument = new XmlDocument();
			XmlElement xmlElement = xmlDocument.CreateElement("customRootNode");
			xmlDocument.AppendChild(xmlElement);
			XmlElement xmlElement2 = xmlDocument.CreateElement("item");
			xmlElement2.SetAttribute("objectType", myObj.GetType().AssemblyQualifiedName);
			XmlDocument xmlDocument2 = new XmlDocument();
			XmlSerializer xmlSerializer = new XmlSerializer(myObj.getType());
			StringWriter writer = new StringWriter();
			xmlSerializer.Serialize(writer, myObj);
			xmlDocument2.LoadXml(writer.ToString());

			Element2.AppendChild(xmlDocument.ImportNode(xmlDocument2.DocumentElement, true));
			xmlElement.AppendChild(xmlElement2);

			File.WriteAllText("C:\\Users\\Public\\multiXML.txt"), xmlDocument.OuterXml);
		}
	}

	public class MyFirstConsoleText{
		private String _text;
		public String text{
			get { return _text; }
			set { _text = value; Console.WriteLine("My first console text class says: " + _text); }
		}
	}

	public class MySecondConsoleText{
		private String _text;
		public String text{
			get{ return _text; }
			set{ _text = value; Console.WriteLine("My second console text class says: " + _text); }
		}
	}
}
