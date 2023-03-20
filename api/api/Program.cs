using api.Configuration;
using api.Repository;
using MongoDB.Driver;

var builder = WebApplication.CreateBuilder(args);
builder.Services.Configure<SicavsStoreConfig>(
builder.Configuration.GetSection("SicavsStoreConfig"));
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
var connectionString = builder.Configuration.GetConnectionString("Mongo");
builder.Services.AddSingleton<IMongoClient>(c =>
{   
    return new MongoClient(connectionString);
});

builder.Services.AddSingleton<ISicavsRepository, SicavsMongoRepository>();

var app = builder.Build();
app.UseSwagger();
app.UseSwaggerUI();

app.MapControllers();

app.UseRouting();

app.Run();

