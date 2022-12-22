/* tslint:disable */
/* eslint-disable */
/**
 * NinjaAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface PodcastEpisodeLightOut
 */
export interface PodcastEpisodeLightOut {
    /**
     * 
     * @type {number}
     * @memberof PodcastEpisodeLightOut
     */
    id: number;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeLightOut
     */
    podcastName: string;
    /**
     * 
     * @type {Date}
     * @memberof PodcastEpisodeLightOut
     */
    date: Date;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeLightOut
     */
    title: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeLightOut
     */
    description: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeLightOut
     */
    audioUrl: string;
    /**
     * 
     * @type {string}
     * @memberof PodcastEpisodeLightOut
     */
    detailsUrl: string;
}

/**
 * Check if a given object implements the PodcastEpisodeLightOut interface.
 */
export function instanceOfPodcastEpisodeLightOut(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "id" in value;
    isInstance = isInstance && "podcastName" in value;
    isInstance = isInstance && "date" in value;
    isInstance = isInstance && "title" in value;
    isInstance = isInstance && "description" in value;
    isInstance = isInstance && "audioUrl" in value;
    isInstance = isInstance && "detailsUrl" in value;

    return isInstance;
}

export function PodcastEpisodeLightOutFromJSON(json: any): PodcastEpisodeLightOut {
    return PodcastEpisodeLightOutFromJSONTyped(json, false);
}

export function PodcastEpisodeLightOutFromJSONTyped(json: any, ignoreDiscriminator: boolean): PodcastEpisodeLightOut {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'podcastName': json['podcast_name'],
        'date': (new Date(json['date'])),
        'title': json['title'],
        'description': json['description'],
        'audioUrl': json['audio_url'],
        'detailsUrl': json['details_url'],
    };
}

export function PodcastEpisodeLightOutToJSON(value?: PodcastEpisodeLightOut | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'podcast_name': value.podcastName,
        'date': (value.date.toISOString().substr(0,10)),
        'title': value.title,
        'description': value.description,
        'audio_url': value.audioUrl,
        'details_url': value.detailsUrl,
    };
}

