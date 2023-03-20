using api.Configuration;
using api.Model;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace api.Repository
{
    public class SicavsMongoRepository : ISicavsRepository
    {
        private readonly IMongoClient _client;
        private readonly IMongoDatabase _database;
        private readonly SicavsStoreConfig _config;
        public SicavsMongoRepository(IMongoClient client, IOptions<SicavsStoreConfig> options)
        {
            this._config = options.Value;
            _client = client;
            _database = this._client.GetDatabase(_config.DatabaseName);
        }

        public async Task<List<Sicav>> GetSicavs(string? isin = null, string? createdDate = null, string? registerNumber = null, string? name = null)
        {
            var collection = _database.GetCollection<Sicav>(_config.MirrorSicavsCollection);
            var query  = collection.AsQueryable();
            if (!string.IsNullOrEmpty(isin))
            {
                query = query.Where(c => c.Isin == isin);
            }
            if (!string.IsNullOrEmpty(createdDate))
            {
                query = query.Where(c => c.RegisterDate == createdDate);
            }
            if (!string.IsNullOrEmpty(registerNumber))
            {
                query = query.Where(c => c.RegisterNumber == registerNumber);
            }
            if (!string.IsNullOrEmpty(name))
            {
                query = query.Where(c => c.Name == name);
            }

            return await query.ToListAsync();
        }
        public async Task<SicavChanges?> GetSicavData(string isin)
        {
            var collection = _database.GetCollection<SicavChanges>(_config.SicavsChangesCollection);
            return await collection.Find(c => c.Isin == isin).FirstOrDefaultAsync();
        }


    }
}
