using api.Model;

namespace api.Repository
{
    public interface ISicavsRepository
    {
        public Task<List<Sicav>> GetSicavs(string? isin = null, string? createdDate = null, string? registerNumber = null, string? name = null);
        public Task<SicavChanges?> GetSicavData(string isin);
    }
}
