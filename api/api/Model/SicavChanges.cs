using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson;

namespace api.Model
{
    public class SicavChanges
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string? Id { get; set; }

        [BsonElement("isin")]
        public string Isin { get; set; }

        [BsonElement("changes")]
        public List<Sicav> Changes { get; set; }
    }
}
