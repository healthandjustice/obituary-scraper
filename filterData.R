nc_releases <- read.csv('./data/NC-1-10-20-2017-2018.csv')
nc_releases <- subset(nc_releases, !is.na(OPUS.NUMBER))
nc_releases <- subset(nc_releases, 
                      TYPE.OF.LAST.MOVEMENT == 'PAROLE/RETURN TO PAR' |
                      TYPE.OF.LAST.MOVEMENT == 'COURT ORDER RELEASE' |  
                      TYPE.OF.LAST.MOVEMENT == 'RELEASED IN ERROR' |
                      TYPE.OF.LAST.MOVEMENT == 'RELEASE PSD')

write.csv(nc_releases, file='./output/filtered_nc_releases_1-10-20.csv')

movement_types <- c('PAROLE/RETURN TO PAR',
                  'COURT ORDER RELEASE',
                  'RELEASED IN ERROR',
                  'RELEASE PSD')
  
counts <- c(nrow(subset(nc_releases, TYPE.OF.LAST.MOVEMENT == 'PAROLE/RETURN TO PAR')),
            nrow(subset(nc_releases, TYPE.OF.LAST.MOVEMENT == 'COURT ORDER RELEASE')),
            nrow(subset(nc_releases, TYPE.OF.LAST.MOVEMENT == 'RELEASED IN ERROR')),
            nrow(subset(nc_releases, TYPE.OF.LAST.MOVEMENT == 'RELEASE PSD')))

count_types_df <- data.frame(movement_types, counts)

write.csv(count_types_df, file='./output/nc_release_movement_types_1-10-20.csv')
