using api.Repository;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace api.Controllers
{
    [Route("api/sicavs")]
    [ApiController]
    public class SicavsController : ControllerBase
    {
        private readonly ISicavsRepository _repository;
        public SicavsController(ISicavsRepository repository)
        {
            _repository = repository;
        }

        [HttpGet]
        [Route("filter")]
        public async Task<IActionResult> Action(
            [FromQuery]string? isin = null, 
            [FromQuery] string? createdDate = null, 
            [FromQuery] string? registerNumber = null, 
            [FromQuery] string? name = null)
        {
            return Ok(await _repository.GetSicavs(isin,createdDate, registerNumber, name ));
        }

        [HttpGet]
        [Route("data")]
        public async Task<IActionResult> Action(
           [FromQuery] string isin)
        {
            return Ok(await _repository.GetSicavData(isin));
        }
    }
}
