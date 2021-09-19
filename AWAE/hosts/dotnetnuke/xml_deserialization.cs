using System;
using System.IO;
using System.Xml.Serialization;
using BasicXMLSerializer

namesapce BasicXMLDeserializer{
	class Program{
		static void Main(strings[] args){
			val fileStream = new FileStream(args[0], FileMode.Open, FileAccess.Read);
			var streamReader = new StreamReader(fileStream);
			XmlSerializer serializer = new XmlSerializer(typeof(MyConsoleText));
			serializer.Deserialize(streamReader);
		}
	}
}
