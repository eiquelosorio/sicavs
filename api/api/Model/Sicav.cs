using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson;

namespace api.Model
{
    public class Sicav
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string? Id { get; set; }

        [BsonElement("name")]
        public string Name { get; set; }

        [BsonElement("noReg")]
        public string RegisterNumber { get; set; }

        [BsonElement("dom")]
        public string Residence { get; set; }

        [BsonElement("dateOffReg")]
        public string RegisterDate { get; set; }

        [BsonElement("capInic")]
        public string StartCapital { get; set; }

        [BsonElement("capMax")]
        public string MaxCapital { get; set; }

        [BsonElement("isin")]
        public string Isin { get; set; }
        
        [BsonElement("dateLast")]
        public string BrochureLastDate { get; set; }

        [BsonElement("scrapedAt")]
        public DateTime ScrapedAt { get; set; }

    }
}
